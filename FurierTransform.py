import matplotlib.pylab as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

p = np.pi
u = complex(0,1)

def FunOnePer(X,i):
    Y = []
    for x in X:
        a = x - i*p
        if (a >= p/2) and (a <= p):
            Y.append(0)
        else:
            Y.append(np.cos(x))
    return Y

def FunManyPer(k):
    FT = []
    F = []
    T = []
    for i in range(-int(k/2),int(k/2+1),1):
        t = np.arange(0+(i*p), p+(i*p), 0.01)
        f = FunOnePer(t,i)
        for j in range(0,len(t)):
            T.append(t[j])
            F.append(f[j])
    FT.append(T)
    FT.append(F)
    return FT

def Fourier(T,N):
    S = []
    for t in T:
        s = 0
        for n in range(1,N+1):
            if (n == 1):
                an = 1/2
                bn = 1/p
            else:
                an = (-n*np.sin(n*p))/(p*(n**2-1))
                bn = (n-n*np.cos(n*p)-2*np.sin(n*p/2))/(p*(n**2-1))
            z = an*np.cos(n*t) + bn*np.sin(n*t)
            s = s + z
        S.append(s)
    return S

def FurAndrey(T,N):
    S = []
    for t in T:
        s = 0
        for n in range(1,N+1):
            '''
            an = (p*n*np.sin(n*p) + np.cos(n*p) - 1)/(p*n)**2
            bn = (np.sin(p*n) - n*p*np.cos(n*p))/(p*n)**2
            z = an*np.cos(2*n*t) + bn*np.sin(2*n*t)
            '''
            #z = np.cos(n*t)*(p*n*np.sin(n*p/2) + 2*np.cos(n*p/2) - 2)*(2/(p*n)**2)
            z = np.sin(n*t)*2*(2*np.sin(n*p/2) - n*p*np.cos(n*p/2))/(n*p)**2
            s = s + z            
        S.append(s + 1/4)
    return S

def FurSin(T,N):
    S = []
    for t in T:
        s = 0
        for n in range(1,N+1):
            if (n == 1):
                bn = 1/p
            else:
                bn = 2*(n- np.sin(n*p/2))/(p*(n**2-1))
            z = bn*np.sin(n*t)
            s = s + z
        S.append(s)
    return S

def FurCos(T,N):
    S = []
    for t in T:
        s = 0
        for n in range(1,N+1):
            if (n == 1):
                an = 1/2
            else:
                an = 2*(-np.cos(n*p/2))/(p*(n**2-1))
            z = an*np.cos(n*t)
            s = s + z
        S.append(s + 1/p)
    return S

def FurIm(T,N):
    SRe = []
    SIm = []
    S = []
    for t in T:
        s = 0
        for n in range(-N,N+1,1):
            if (abs(n) == 1):
                cn = (p-2*u)/(4*p)
            else:
                if(n == 0):
                    cn = 0
                else:
                    cn = (u*n+np.e**(-1/(2*p*u*n))-u*np.e**(u*n*p)-np.e**(u*n*p/2))/(2*p*(1-n**2))                    
            z = cn*np.e**(u*n*t)
            s = s + z
        SRe.append(s.real)
        SIm.append(s.imag)
        #S.append((s.real**2 + s.imag**2)**0.5)
        S.append(s.real)
    return S

T = np.arange(-4*p, 4*p, 0.01)
S = FurIm(T,100)
plt.plot(T,S)
'''
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(T,S[0],S[1])
'''
plt.xlabel('t')
plt.ylabel('f(t)')
plt.show()

