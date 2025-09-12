s = input()

alpha = 'abcdefghijklmnopqrstuvwxyz'

arr = []
for i in alpha:
    num = -1
    for j in range(len(s)):
        if i == s[j]:
            if num == -1:
                num = j
    arr.append(num)

for i in arr:
    print(i, end=" ")