if __name__=="__main__":
    T=int(input())
    for t in range(T):
        n,k=[int(i) for i in input().split()]
        if k < n-1:
            print(n)
        else:
            print(1)