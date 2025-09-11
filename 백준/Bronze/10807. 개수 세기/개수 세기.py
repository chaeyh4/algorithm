n = int(input())

arr = input().split()

v = input()

cnt = 0

for i in range(n):
    if arr[i] == v:
        cnt += 1

print(cnt)