import sys
from collections import deque

input = sys.stdin.readline

def bfs(table, start_x, start_y, n, m):
    queue = deque()
    queue.append((start_x, start_y))
    table[start_x][start_y] = -1  # 방문 처리

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and table[nx][ny] == 1:
                table[nx][ny] = -1
                queue.append((nx, ny))


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        m, n, k = map(int, input().split())
        table = [[0] * m for _ in range(n)]

        for _ in range(k):
            x, y = map(int, input().split())
            table[y][x] = 1  # y가 행, x가 열

        count = 0

        for i in range(n):
            for j in range(m):
                if table[i][j] == 1:
                    bfs(table, i, j, n, m)
                    count += 1

        print(count)
