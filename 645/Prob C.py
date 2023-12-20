sum=1
def findPath(x1,y1,x2,y2):
    global sum
    if x1==x2 or y1==y2:
        return
    if x1+1<=x2:
        findPath(x1+1,y1,x2,y2)
    if y1+1<=y2:
        findPath(x1,y1+1,x2,y2)
        sum+=1


if __name__=="__main__":
    T=int(input())
    for t in range(T):
        sum=1
        x,y,z,w=[int(i) for i in input().split()]
        findPath(x,y,z,w)

        print(sum)