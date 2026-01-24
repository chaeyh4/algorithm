import sys
from collections import deque

input = sys.stdin.readline

def bfs(maze, start):
    queue = deque([start])
    x, y = start
    maze[x][y] == -1
    directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,-1),(-1,1)]
    while queue:
        pos_x, pos_y = queue.popleft()
        for dx, dy in directions:
            nx = pos_x + dx
            ny = pos_y + dy
            if 0<=nx<h and 0<=ny<w and maze[nx][ny] == 1:
                maze[nx][ny] = -1
                queue.append((nx,ny))


    
    

if __name__ == "__main__":
    while True:
        w, h = map(int,input().rstrip().split())
        if w == 0 and h == 0:
            break
        maze = [list(map(int,input().rstrip().split())) for _ in range(h)]
        #print(maze)
        cnt = 0
        for i in range(h):
            for j in range(w):
                #print(maze[i][j])
                if maze[i][j] == 1:
                    start = (i,j)
                    bfs(maze,start)
                    cnt += 1
        print(cnt)
                    
        
    