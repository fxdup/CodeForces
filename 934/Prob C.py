if __name__=="__main__":
    T=int(input())
    for t in range(T):
        l = int(input())
        a=sorted([int(i) for i in input().split()])
        c = [False for i in range(max(a)+2)]
        while a:
            c[a.pop(-1)] = True
            a.pop(-1)

        if a:
            c[a.pop(-1)] = True

        print(c.index(False))
        

