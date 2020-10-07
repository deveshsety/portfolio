for i in range(int(input())):
    cost_of_green,cost_of_blue = sorted(list(map(int,input().strip().split())))
    m = 0
    n = 0
    for p in range(int(input())):

        a,b = list(map(int,input().strip().split()))
        if (a==1 and b==1) :
            m += 1
            n += 1
        elif a==1 and b==0:
            m += 1
        elif b == 1 and a==0:
            n +=1
    if m > n or m == n:
        print(m*cost_of_green + n*cost_of_blue)
    elif m < n :
        print(n*cost_of_green + m*cost_of_blue)