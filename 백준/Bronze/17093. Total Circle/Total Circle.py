import sys
input = sys.stdin.readline

n, m = map(int, input().split())

P = [tuple(map(int, input().split())) for _ in range(n)]
Q = [tuple(map(int, input().split())) for _ in range(m)]

answer = 0

for px, py in P:
    for qx, qy in Q:
        dist_sq = (px - qx) ** 2 + (py - qy) ** 2
        if dist_sq > answer:
            answer = dist_sq

print(answer)