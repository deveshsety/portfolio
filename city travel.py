from math import ceil

s, x, n = list(map(int, input().split()))

ty = []
for _ in range(n):
    ty.append(list(map(int, input().split())))
    # ty[t_i] = y_i

ty.sort(key=lambda x: x[0])

i = 0

ty = iter(ty)

while s > 0:
    crnt = next(ty, None)
    if crnt == None:
        i += ceil(s / x)
        break

    print(s, crnt)
    if s > (crnt[0] - (i + 1)) * x:
        s -= (crnt[0] - (i + 1)) * x
        s -= crnt[1]
        i += ((crnt[0] - (i + 1)) + 1)
    else:
        i += ceil(s / x)
        break

print(i)