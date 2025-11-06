import sys 
from collections import deque

input = sys.stdin.readline

deq = deque()


n = int(input())

for _ in range(n):
    order = input().split()
    w_order = order[0]
    if w_order == "1":
        deq.appendleft(order[1])
    elif w_order == "2":
        deq.append(order[1])
    elif w_order == "3":
        if deq:
            print(deq.popleft())
        else:
            print("-1")
    elif w_order == "4":
        if deq:
            print(deq.pop())
        else:
            print("-1")
    elif w_order == "5":
        print(len(deq))
    elif w_order == "6":
        if deq:
            print("0")
        else:
            print("1")
    elif w_order == "7":
        if deq:
            print(deq[0])
        else:
            print("-1")
    elif w_order == "8":
        if deq:
            print(deq[-1])
        else:
            print("-1")