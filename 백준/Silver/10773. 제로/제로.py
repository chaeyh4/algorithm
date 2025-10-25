import sys
input = sys.stdin.readline
k = int(input().strip())

k_list = []
for _ in range(k):
    n = int(input())
    if n != 0:
        k_list.append(n)
    if n == 0:
        k_list = k_list[:-1]

print(sum(k_list))