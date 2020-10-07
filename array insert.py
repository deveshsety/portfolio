a,n = input().strip().split()
a = list(a)
arr = list(map(int,input().strip().split()))

for i in range(int(n)):
    q,r,l = list(map(int,input().strip().split()))
    sum = 0
    if q == 1 :
        arr[r] = l
    elif q == 2 :
        for item in range(r,l+1,+1):
            sum += int(arr[item])
        print(sum)


