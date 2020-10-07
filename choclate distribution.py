from math import floor
T = int(input())

for i in range(T):
    c,n = map(int,input().split())

    k = floor((2*c - n*(n-1))/(2*n))
    if k<1:
        print(c)
    else:
        print(int(c - n*(2*k + n - 1)//2))

