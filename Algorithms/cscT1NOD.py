def nod(a,b):
    r = b%a
    if r == 0:
        return a
    else:
        return nod(r,a)
    
def csc1(n):
    s = 0
    nods = []
    for i in range(1,n):
        for j in range(i+1,n):
            a = 2**i + 1
            b = 2**j + 1
            q = nod(a,b)
            if q not in nods:
                s = s + q
                nods.append(q)
    return s

def csc2(n):
    s = 0
    for i in range(1,n):
        for j in range(i+1,n):
            a = 2**i + 1
            b = 2**j + 1
            q = nod(a,b)
            s = s + q
    return s

print(csc1(2020))
