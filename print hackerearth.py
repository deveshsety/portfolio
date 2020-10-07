n = int(input())
s = input()
d = {}
l = ['h', 'a', 'e', 'r']
l1 = set(s)
print(l1)
for i in l1:
    d[i] = s.count(i)
    if i in l:
        d[i] = d[i]//2
print(min(d.values()))