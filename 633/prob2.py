T=int(input())
for t in range(T):
    n,a,b =[int(i) for i in input().split()]
    letter=97
    currentString=""
    ans=""
    count=1
    for i in range(n):
        ans+=chr(letter)
        if count<b:
            letter+=1
            count+=1
        elif len(ans)>=a and b>1:
            if ans[i-a+2]!=ans[i-a+1]:
                letter += 1
    print(ans)