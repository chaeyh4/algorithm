import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    by_type = {}
    for _ in range(n):
        name, kind = input().split()
        by_type[kind] = by_type.get(kind, 0) + 1
    total = 1
    for cnt in by_type.values():
        total *= (cnt + 1)

    print(total - 1)