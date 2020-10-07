import math


for _ in range(int(input())):
    r,l,s = list(map(int,input().strip().split()))
    x = math.ceil(r/s)
    y = math.floor(l/s)
    if x > y :
        print(-1,-1)
    else:
        print(x,y)
