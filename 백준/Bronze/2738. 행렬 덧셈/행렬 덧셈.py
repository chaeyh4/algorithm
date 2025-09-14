n, m = map(int, input().split())

a = []
b = []

for i in range(n):
    arr = input().split()
    a.append(arr)

for i in range(n):
    arr = input().split()
    b.append(arr)

c = []
for i in range(n):
    arr_c = []
    for j in range(m):
        arr_c.append(int(a[i][j])+int(b[i][j]))
    c.append(arr_c)

for i in range(n):
    for j in range(m):
        print(c[i][j], end = ' ')
    print()