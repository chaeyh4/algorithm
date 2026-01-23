import sys
from collections import deque

input = sys.stdin.readline

def bfs(maze,start,visited):
    global cnt
    queue = deque([start])
    x, y = start
    visited[x][y] = True

    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    while queue:
        pos_x, pos_y = queue.popleft()
        #print(pos_x,pos_y)
        visited[pos_x][pos_y] = True
        for dx, dy in directions:
            nx = dx+pos_x
            ny = dy+pos_y
            if 0<=nx<n and 0<=ny<m and maze[nx][ny] != 'X' and visited[nx][ny]==False:
                visited[nx][ny] = True
                if maze[nx][ny] == 'P':
                    cnt += 1
                queue.append((nx,ny))

    return cnt


if __name__ == "__main__":
    n,m = map(int,input().split())
    maze = [list(input().strip()) for _ in range(n)]
    #print(maze)
    cnt = 0
    visited = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'I':
                start = (i,j)
                visited[i][j] = True
                break
    people_cnt = bfs(maze,start,visited)
    if people_cnt == 0:
        print('TT')
    else:
        print(people_cnt)