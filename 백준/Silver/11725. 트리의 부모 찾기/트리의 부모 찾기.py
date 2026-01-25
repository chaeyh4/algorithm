import sys
input = sys.stdin.readline

def dfs(graph, start, visited):
    visited[start] = True
    stack = [start]

    while stack:
        node = stack.pop()
        visited[node] = True
        for next_node in graph[node]:
            if visited[next_node] == False:
                visited[next_node] = True
                stack.append(next_node)
                
                #print(next_node, node)
                parents[next_node] = node

    

if __name__ == "__main__":
    n = int(input())
    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    for _ in range(n-1):
        n1, n2 = map(int,input().rstrip().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    for i in range(1,n+1):
        graph[i].sort()
    #print(graph)
    parents = [0] * (n+1)
    dfs(graph,1,visited)
    #print(parents)
    for i in range(2,n+1):
        print(parents[i])