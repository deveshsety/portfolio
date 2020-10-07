from collections import Counter

for test_cases in range(int(input())):
    s1 =list(input())
    s2 = list(input())
    x = Counter(s1)
    y = Counter(s2)
    x.subtract(y)
    print(sum(abs(i) for i in x.values()))