if __name__=="__main__":
    T=int(input())
    for t in range(T):
        n = int(input())
        a = [int(i) for i in input().split()]
        print(len(a)-len(set(a)))