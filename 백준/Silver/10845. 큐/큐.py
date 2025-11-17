import sys
from collections import deque


if __name__ == "__main__":
    input = sys.stdin.readline
    queue = deque()
    n = int(input())
    for _ in range(n):
        order = list(input().split())
        type_ = order[0]
        if type_ == "push":
            queue.append(int(order[1]))
        elif type_ == "pop":
            if queue:
                print(queue[0])
                queue.popleft()
            else:
                print(-1)
        elif type_ == "size":
            print(len(queue))
        elif type_ == "empty":
            if queue:
                print(0)
            else:
                print(1)
        elif type_ == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif type_ == "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)