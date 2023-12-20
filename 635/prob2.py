T=int(input())
for t in range(T):
    x,m,n =[int(i) for i in input().split()]
    defeated=False
    while not defeated and (m>0 or n>0):
        if (int(x/2) + 10 < x and m>0) or (n==0 and m>0):
            x=int(x/2)+10
            m-=1
        else :
            x=x-10
            n-=1
        if x<=0:
            defeated=True
    print("YES" if defeated else "NO")