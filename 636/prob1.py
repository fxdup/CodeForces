T=int(input())
for t in range(T):
    found=False
    n = int(input())
    x=int(n/2)+1
    while not found:
        sum=0
        k=1
        x-=1
        if n%x!=0:
            continue
        s=int(n/x)
        if '0' not in str(bin(s))[2:]:
            print(x)
            break