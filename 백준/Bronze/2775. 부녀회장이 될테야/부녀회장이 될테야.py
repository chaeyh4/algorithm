import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())  # 층
    n = int(input())  # 호수

    apart = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, n + 1):
        apart[0][i] = i

    for floor in range(1, k + 1):
        for room in range(1, n + 1):
            # a층 b호 = a층 (b-1)호 + (a-1)층 b호
            apart[floor][room] = apart[floor][room - 1] + apart[floor - 1][room]

    print(apart[k][n])