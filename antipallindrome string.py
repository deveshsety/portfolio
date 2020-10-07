for _ in range(int(input())):
    s = list(input())
    a =""
    if s == s[::-1]:
        print(-1)
    else:
        s.sort()
        print(a.join(s))
