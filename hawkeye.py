n = int(input())

it, jt, p = list(map(int, input().split(' ')))

for i in range(n):
    for j in range(n):
        print("%d " % max(p - (max(abs(it - i), abs(jt - j))), 0), end=' ')
    print()