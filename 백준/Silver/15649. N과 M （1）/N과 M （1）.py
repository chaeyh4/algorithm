import sys
import itertools

input = sys.stdin.readline
n, m = map(int, input().split())

for seq in itertools.permutations(range(1, n + 1), m):
    print(*seq)