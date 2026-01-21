'''
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.
'''

import sys
input = sys.stdin.readline


def bfs(graph, start, visited):
    queue = [start]

    while queue:
        node = queue.pop(0)
        visited[node] = True
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)




if __name__ == "__main__":
    n, m = map(int,input().split())
    visited = [False]*(n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1,n+1):
        graph[i].sort()
    cnt = 0
    for i in range(1,n+1):
        if visited[i] == False:
            bfs(graph, i, visited)
            cnt += 1
    print(cnt)

    