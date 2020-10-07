l = int(input())
for i in range(int(input())):
    w,l1 = input().split(" ")

    if int(w) >= l and int(l1) >= l:
        if (int(w) == int(l1)) or (int(w)==l and int(l1)==l):
            print("ACCEPTED")
        else:
            print("CROP IT")
    else :
        print("UPLOAD ANOTHER")