n = int(input())
array1 = input()
if "HH" in array1 :
    print("NO")
else :
    print("YES")
    array1 = array1.replace(".","B")
    print(array1)