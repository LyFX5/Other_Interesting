def katiaNum(x):
    s = str(x)
    if "1" in s and "3" in s and len(s) > 1:
        one = s.index("1")
        ss = s[one:len(s)]
        if "3" in ss:
            return False
        else:
            return True
    else:
        return True

def prime(x):
    i = 2
    while i <= x**(1/2):
        if x%i == 0:
            return False
        i += 1
    return True

def chek(a,b):
    r = 0
    for i in range(a,b+1):
        if prime(i) and katiaNum(i):
            r += 1
    return r

s = input().split(" ")
a = int(s[0])
b = int(s[1])
print(chek(a,b))

