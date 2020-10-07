str1 = ""
s = list(input())
l =len(s)
for i in range(l):
    if s[i] == s[i].upper():
        s[i] = s[i].lower()
    else :
        s[i] = s[i].upper()
for ele in s:
    str1 += ele
print(str1)

