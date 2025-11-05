import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    order = input().split()
    if order[0] == "push":
        q.append(order[1])
    elif order[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif order[0] == "size":
        print(len(q))
    elif order[0] == "empty":
        print(0 if q else 1)
    elif order[0] == "front":
        print(q[0] if q else -1)
    elif order[0] == "back":
        print(q[-1] if q else -1)