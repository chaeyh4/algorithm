import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph, start, visited, virus_count=0):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                virus_count += 1
                queue.append(neighbor)
    return virus_count
                

if __name__ == "__main__":
    com_num = int(input())
    pair_num = int(input())
    pair_list = []
    for _ in range(pair_num):
        pair_list.append(list(map(int, input().split())))
    #print(pair_list)
    graph = [[] for _ in range(com_num + 1)]
    for pair in pair_list:
        graph[pair[0]].append(pair[1])
        graph[pair[1]].append(pair[0])
    visited = [False] * (com_num + 1)
    print(bfs(graph, 1, visited))
    