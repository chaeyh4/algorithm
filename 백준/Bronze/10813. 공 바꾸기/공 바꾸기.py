n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(i+1)

for cnt in range(m):
    i, j = map(int, input().split())
    tmp = arr[i-1]
    arr[i-1] = arr[j-1]
    arr[j-1] = tmp

for i in arr:
    print(i, end=" ")