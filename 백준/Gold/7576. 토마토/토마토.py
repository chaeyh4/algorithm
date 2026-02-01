import sys
from collections import deque

input = sys.stdin.readline

def bfs(farm, visited, queue, n, m):
    global day
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        day += 1  

        for _ in range(len(queue)):  
            x, y = queue.popleft()

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                # 밖으로 나가면 안됨, 방문했으면 안됨, 익지 않은 토마토(0)만 익힘
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and farm[nx][ny] == 0:
                    visited[nx][ny] = True
                    farm[nx][ny] = 1
                    queue.append((nx, ny))

if __name__ == "__main__":
    m, n = map(int, input().split())
    farm = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    day = -1 

    queue = deque()

    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                queue.append((i, j))
                visited[i][j] = True

    bfs(farm, visited, queue, n, m)

    for i in range(n):
        for j in range(m):
            if farm[i][j] == 0:
                print(-1)
                sys.exit(0)

    print(day)