if __name__=="__main__":
    T=int(input())
    for t in range(T):
        k,q=[int(i) for i in input().split()]
        a_ori=[int(i) for i in input().split()]
        n=[int(i) for i in input().split()]
        res = []
        for n_i in range(len(n)):
            a = a_ori.copy()
            while(a):
                for idx in range(len(a)-1,-1,-1):
                    if a[idx] > n[n_i]:
                        a.pop(idx)
                n[n_i] -= len(a)

        print(" ".join([str(i) for i in n]))