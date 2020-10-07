t = int(input())
for i in range(t):
    seat_no = int(input())
    remainder = 12 % seat_no
    if seat_no == 1 or remainder == 1:
        print(f"{seat_no+11} WS")
    elif seat_no == 2 or remainder == 2:
        print(f"{seat_no+9} MS")
    elif seat_no == 3 or remainder == 3:
        print(f"{seat_no+7} AS")
    elif seat_no == 4 or remainder == 4 :
        print(f"{seat_no+5} AS")
    elif seat_no == 5 or remainder == 5:
        print(f"{seat_no+3} MS")
    elif seat_no == 6 or remainder == 6:
        print(f"{seat_no+1} WS")
    elif seat_no == 7 or remainder == 7:
        print(f"{seat_no-1 } WS")
    elif seat_no == 8 or remainder == 8:
        print(f"{seat_no-3} MS")
    elif seat_no == 9 or remainder == 9:
        print(f"{seat_no-5} AS")
    elif seat_no == 10 or remainder == 10:
        print(f"{seat_no-7} AS")
    elif seat_no == 11 or remainder == 11:
        print(f"{seat_no-9} MS")
    elif seat_no == 12 or remainder == 0 :
        print(f"{seat_no-11} WS")
    else:
        print(0)