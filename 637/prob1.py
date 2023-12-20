T=int(input())
for t in range(T):
    n,a,b,c,d = [int(i) for i in input().split()]
    print("Yes" if (n*(a-b)>=c-d and n*(a-b)<=c+d) or (n*(a+b)>=c-d and n*(a+b)<=c+d) or (n*(a-b)>=c-d and n*(a+b)<=c-d) or (n*(a-b)>=c+d and n*(a+b)<=c+d) else "No")