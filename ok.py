s = str(input("enter the string of brackets : "))
c1 = 0
c2 = 0
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
    else :
        print("the sequence is incorrect")
else :
    print("enter a string under 5000000 characters")

