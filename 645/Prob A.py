
if __name__=="__main__":
    T=int(input())
    for t in range(T):
        n,m=[int(i) for i in input().split()]
        if n%2==0 or m%2==0:
            print(int(n*m/2))
        else:
            print(int(n*m/2)+1)