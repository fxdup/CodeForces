T=int(input())
for t in range(T):
    r,g,b=input().split()
    rweight=[int(i) for i in input().split()]
    gweight=[int(i) for i in input().split()]
    bweight=[int(i) for i in input().split()]
    if len(rweight)<len( gweight) and len(rweight)<len(bweight):
        set1=rweight
    else :
        set1=gweight if len(gweight)<len(bweight) else bweight
    if len(rweight)>=len( gweight) and len(rweight)>=len(bweight):
        set2=rweight
    else :
        set2=gweight if len(gweight)>=len(bweight) else bweight
    set3=rweight if not (set1==rweight or set2 == rweight) else gweight if not (set1==gweight or set2 == gweight) else bweight
    min=-1
    done=set()
    for i in sorted(set1):
        for j in sorted(set3):
            if (i,j) not in done:
                done.add((i,j))
            else : continue
            for k in sorted(set2):
                result=(i-j)**2+(j-k)**2+(k-i)**2
                if min==-1 or min>result:
                    min=(i-j)**2+(j-k)**2+(k-i)**2
    print(min)