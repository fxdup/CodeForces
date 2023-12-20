if __name__=="__main__":
    T=int(input())
    for t in range(T):
        input()
        arr=sorted([int(i) for i in input().split()])
        l=len(arr)
        while l>0 and arr[-1]>l:
            arr.pop()
            l-=1

        print(l+1)