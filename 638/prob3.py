T=int(input())
for t in range(T):
    n,k = [int(i) for i in input().split()]
    arr=['' for i in range(k)]
    sortedStr=sorted(input())
    for ind,i in enumerate(sortedStr):
        arr[ind%k]+=i
    print(max(arr))