if __name__=="__main__":
    T=int(input())
    for t in range(T):
        n=[int(i) for i in input().split()]
        tree = [[] for i in n]
        tree_color = [False for i in n]
        for i in n:
            u,v=[int(i) for i in input().split()]
            tree[u].append(v)
            tree[v].append(u)