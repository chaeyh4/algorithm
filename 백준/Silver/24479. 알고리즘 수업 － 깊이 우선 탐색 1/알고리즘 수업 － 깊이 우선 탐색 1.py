import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(graph, start, visited, order, cnt):
    visited[start] = True
    order[start] = cnt[0]

    for next_node in graph[start]:
        if not visited[next_node]:
            cnt[0] += 1
            dfs(graph, next_node, visited, order, cnt)

if __name__ == "__main__":
    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    order = [0] * (n+1)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, n+1):
        graph[i].sort()

    cnt = [1]
    dfs(graph, r, visited, order, cnt)

    for i in range(1, n+1):
        print(order[i])
