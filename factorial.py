def Factorial(x):
    factorial = 1
    for i in range(x,0,-1):
        factorial = factorial*i
    print(factorial)


Factorial(int(input()))

