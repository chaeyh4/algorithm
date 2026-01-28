import sys
from collections import deque
input = sys.stdin.readline

def bfs(maze, visited, start):
    queue = deque([start])
    x, y = start
    visited[x][y] = 0
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

if __name__ == "__main__":
    n, m = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(n)]
    visited = [[-1] * m for _ in range(n)]

    start = None
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 2:
                start = (i, j)
                break
        if start is not None:
            break

    bfs(maze, visited, start)

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 0:          
                print(0, end=" ")
            else:                       
                print(visited[i][j], end=" ")
        print()
