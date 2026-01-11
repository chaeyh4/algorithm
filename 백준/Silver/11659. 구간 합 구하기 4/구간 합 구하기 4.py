import sys
input = sys.stdin.readline

n, m = map(int, input().split())
n_list = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + n_list[i - 1]

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i - 1])