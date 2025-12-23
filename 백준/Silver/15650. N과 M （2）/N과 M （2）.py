import sys
input = sys.stdin.readline

def dfs(start, path):
    if len(path) == m:
        print(*path)
        return
    
    for i in range(start, n + 1):
        dfs(i + 1, path + [i])

if __name__ == "__main__":
    n, m = map(int, input().split())
    dfs(1, [])