import sys; input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
coords = [list(map(int, input().split())) for _ in range(k)]

matrix = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        matrix[i][j] = (
            matrix[i - 1][j]
            + matrix[i][j - 1]
            + arr[i - 1][j - 1]
            - matrix[i - 1][j - 1]
        )

for i, j, x, y in coords:
    print(
        matrix[x][y]
        - (matrix[x][j - 1] + matrix[i - 1][y])
        + matrix[i - 1][j - 1]
    )