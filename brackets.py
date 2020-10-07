s = str(input("enter the string of brackets : "))
c1 = 1
c2 = 1
n = len(s)
print(f"the no. of characters in string {n}")
n1 = 0
if n < 500000:
    for i in s:
        if i == "(":
            c1 += 1
        elif i == ")":
            c2 += 1
        else :
            print("the entered string contains something other than brackets")
    if c1 == c2:
        n1 = n/2
        print(f"the no. of bracket pair is : {n1}")
    elif c1 < c2 :
       a1 = c2 - c1
       print(a1)
    elif c2<c1 :
        a2= c1-c2
        print(a2)
    else :     print("the sequence is incorrect")
else :
    print("enter a string under 5000000 characters")
