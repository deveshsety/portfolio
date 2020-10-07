h = int(input())
s = input()
d = {}
x = set(s)
print(x)
l = ["h","a","e","r",]
for i in x :
    d[i] = s.count(i)
    if i in l :
        d[i] = s.count(i)/2
print(min(d.values()))
