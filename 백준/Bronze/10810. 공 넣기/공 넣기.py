n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(0)

for num in range(m):
    i, j, k = map(int, input().split())
    for bas in range(i,j+1,1):
        arr[bas-1] = k

for i in arr:
    print(i, end = " ")