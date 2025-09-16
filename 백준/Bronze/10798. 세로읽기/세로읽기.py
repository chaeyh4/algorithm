arr = []
max = 0
for i in range(5):
    list_x = list(input())
    arr.append(list_x)
    if len(list_x) > max:
        max = len(list_x)
for i in arr:
    if len(i) < max:
        num = max - len(i)
        for j in range(num):
            i.append("*")

for j in range(max):
    for i in range(5):
        if arr[i][j] != "*":
            print(arr[i][j], end="")
        else:
            pass