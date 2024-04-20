from itertools import combinations 

def xor(l):
    res = l[0]
    for i in range(1,len(l)):
        res = res ^ l[i]
    return res

if __name__=="__main__":
    T=int(input())
    for t in range(T):
        found = False
        n,k=[int(i) for i in input().split()]
        a=[int(i) for i in input().split()]
        x_possibilities = list(combinations(a[:n], 2*k))
        y_possibilities = list(combinations(a[n:], 2*k))
        for x_pos in x_possibilities:
            x_xor = xor(x_pos)
            for y_pos in y_possibilities:
                y_xor = xor(y_pos)
                if x_xor == y_xor:
                    print(*x_pos)
                    print(*y_pos)
                    found = True
                    break
            if found:
                break
