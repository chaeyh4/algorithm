import sys
from collections import deque
input = sys.stdin.readline

def bfs(maze,start):
    queue = deque()
    queue.append(start)
    x = start[0]
    y = start[1]
    maze[x][y] = -1
    count = 1

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    

    while queue:
        x,y = queue.popleft()
        apart.append((x,y))
        for dx,dy in directions:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n and maze[nx][ny] == 1:
                maze[nx][ny] = -1
                
                queue.append((nx,ny))
                count += 1
    return count





if __name__ == "__main__":
    n = int(input())
    maze = [list(map(int,input().rstrip())) for _ in range(n)]
    result = []
    #print(maze)
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 1:
                apart = []
                result.append(bfs(maze,(i,j)))

    result.sort()
    print(len(result))
    for i in result:
        print(i)