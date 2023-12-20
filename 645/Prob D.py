if __name__=="__main__":
    n,x=[int(i) for i in input().split()]
    days=[int(i) for i in input().split()]
    cal=[]
    for d in days:
        for i in range(1,d+1):
            cal.append(i)
    i= -x
    max=0
    while i+x<len(cal):
        if i<0:
            nmax=sum(cal[len(cal)+i:])+sum(cal[:i+x])

        else: nmax=sum(cal[i:i+x])
        if nmax>max:
            max=nmax
        i+=1
    print(max)