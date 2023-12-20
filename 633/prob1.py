import math
T=int(input())
for t in range(T):
    n = int(input())
    if n%2:
        print(int(n/2))
    else: print (int(n/2)-1)