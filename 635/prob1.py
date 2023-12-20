import math
T=int(input())
for t in range(T):
    a, b, c, d = input().split()
    a=int(a)
    b = int(b)
    c = int(c)
    d= int(d)
    found=False
    for z in range(c,d+1):
        if found:
            break
        for y in reversed(range(b,c+1)):
            if found:
                break
            for x in reversed(range(a,b+1)):
                if found:
                    break
                if z<x+y:
                    print(x,y,z)
                    found=True