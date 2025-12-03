import sys
from collections import deque


input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    d_list = deque()
    for _ in range(n):
        order = list(input().rstrip().split())
        if order[0] == "push_front":
            d_list.appendleft(int(order[1]))
        elif order[0] == "push_back":
            d_list.append(int(order[1]))
        elif order[0] == "pop_front":
            if d_list:
                print(d_list.popleft())
            else:
                print(-1)
        elif order[0] == "pop_back":
            if d_list:
                print(d_list.pop())
            else:
                print(-1)
        elif order[0] == "size":
            print(len(d_list))
        elif order[0] == "empty":
            if d_list:
                print(0)
            else:
                print(1)
        elif order[0] == "front":
            if d_list:
                print(d_list[0])
            else:
                print(-1)
        elif order[0] == "back":
            if d_list:
                print(d_list[-1])
            else:
                print(-1)