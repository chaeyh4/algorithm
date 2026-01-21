import sys
input = sys.stdin.readline

def dfs(graph, start, visited):
    stack = [start]
    visited[start] = True

    while stack:
        node = stack.pop()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append(next_node)

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            dfs(graph, i, visited)
            cnt += 1

    print(cnt)
