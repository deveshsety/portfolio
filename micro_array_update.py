t = int(input(" "))
for i in range(0,t):
    b = list(map(int, input(" ").strip().split()))
    a = list(map(int,input(" ").strip().split()))

    n = b[0]
    k = b[1]
    l=len(a)
    if l == n :
        min = a[0]
        for j in range(0, l):
            if min > a[j] :
                min == a[j]
        if min < k :
            print(k-min)
        else :
            print(0)
    else:
        print(0)