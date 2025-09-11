n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(i+1)
for cnt in range(m):
    i, j = map(int, input().split())
    rep = j - i + 1
    copy_arr = arr[:]
    for k in range(rep):
        arr[i+k-1] = copy_arr[j-k-1]

for i in arr:
    print(i, end = " ")