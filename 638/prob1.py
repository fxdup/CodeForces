T=int(input())
for t in range(T):
    n = int(input())
    pile1=0
    pile2=0
    if n==2:
        print(2)
    else:
        for i in range(1,int(n/2)+1):
            if(i%2):
                pile1+=2**i + 2**(n-i+1)
            else: pile2 += 2 ** i + 2 ** (n - i + 1)
        print(abs(pile1-pile2))