c = 0
n = int(input())
b = 0
a = list(map(int,input("").strip().split()))
l1 = len(a)
if l1 == n :
    for i in range(0,l1):
        for b in range(0,l1):
            if a[i]+1 == a[b]:
                c += 1

    print(c)
else:
    print(0)
