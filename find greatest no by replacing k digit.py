s,k = list(input().strip().split())
s = list(s)
k = int(k)
a = ""


for _ in range(len(s)):
    if k != 0 :
        if s[_] != "9":
            s[_] = "9"
            k -= 1
print(a.join(s))
