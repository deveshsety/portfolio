for t in range(int(input())):
    s = input()
    vowels = "aeiou"
    c = 0
    res = [s[i:j] for i in range(len(s))for j in range(i+1,len(s)+1)]
    for m in res:
        for n in m :
            if n.lower() in vowels :
                c += 1
    print(c)

# without getting the real subset
# for _ in range(int(input())):
#     string = input()
#     vowels, length = 0, len(string)
#     for i in range(length):
#         if string[i].lower() in 'aeiou':
#             vowels += (length - i) * (i + 1)
#     print(vowels)