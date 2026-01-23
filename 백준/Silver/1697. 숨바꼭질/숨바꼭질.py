import sys
from collections import deque

input = sys.stdin.readline

def bfs(n, k):
    visited = [False] * 100001
    queue = deque()
    queue.append((n, 0)) 
    visited[n] = True

    while queue:
        location, time = queue.popleft()

        if location == k:
            return time

        for next_pos in (location - 1, location + 1, location * 2):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(bfs(n, k))