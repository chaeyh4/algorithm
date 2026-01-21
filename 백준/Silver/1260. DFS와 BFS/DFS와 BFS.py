import sys
input = sys.stdin.readline

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=" ")
    for next_node in graph[start]:
        if not visited[next_node]:
            dfs(graph, next_node, visited)

def bfs(graph, start, visited):
    queue = [start]
    visited[start] = True
    print(start, end=" ")

    while queue:
        node = queue.pop(0)
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                print(next_node, end=" ")
                queue.append(next_node)

if __name__ == "__main__":
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n+1):
        graph[i].sort()

    visited = [False] * (n+1)
    dfs(graph, v, visited)

    print()

    visited = [False] * (n+1)
    bfs(graph, v, visited)
