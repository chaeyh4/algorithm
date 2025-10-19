import sys
input = sys.stdin.readline
n, m = map(int,input().split())

n_set = set()
for _ in range(n):
    string_n = input()
    n_set.add(string_n)

cnt = 0
for _ in range(m):
    string_m = input()
    if string_m in n_set:
        cnt += 1

print(cnt)