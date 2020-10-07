s = input()
a = ["0","1","2","3","4","5","6","7","8","9"]
a1,b1,c1,d1,e1,f1,g1,h1,i1,k1 = [0,0,0,0,0,0,0,0,0,0,]

for i in s :
    if i == "0":
        a1 += 1
    elif i == "1":
        b1 += 1
    elif i =="2":
        c1 += 1
    elif i == "3":
        d1 += 1
    elif i == "4":
        e1 += 1
    elif i == "5":
        f1 += 1
    elif i == "6":
        g1 += 1
    elif i == "7":
        h1 += 1
    elif i == "8":
        i1 += 1
    elif i == "9":
        k1 += 1
x = [a1,b1,c1,d1,e1,f1,g1,h1,i1,k1]
for m in range(len(a)):
    print(a[m],x[m])