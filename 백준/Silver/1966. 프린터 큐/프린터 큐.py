import sys
from collections import deque

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        n, m = map(int, input().split())
        importance = list(input().split())
        importance_deque = deque()
        for i in range(n):
            importance_deque.append((i,importance[i]))
        cnt = 0
        while importance_deque:
            check = importance_deque[0][1]
            index = importance_deque[0][0]
            max_im = []
            for i in range(0,len(importance_deque)):
                max_im.append(importance_deque[i][1])
            if check >= max(max_im):
                importance_deque.popleft()
                cnt += 1
                if index == m:
                    print(cnt)
                    break
            else:
                importance_deque.popleft()
                importance_deque.append((index, check))