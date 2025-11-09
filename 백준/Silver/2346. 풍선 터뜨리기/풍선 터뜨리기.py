import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
balloon = deque(range(1,n+1))
while len(balloon) >= 1:
    cur = balloon.popleft()
    print(cur, end = " ")
    if not balloon:
        break
    if n_list[cur-1] > 0:
        for i in range(n_list[cur-1]-1):
            balloon.append(balloon.popleft())
    else:
        for i in range(abs(n_list[cur-1])):
            balloon.appendleft(balloon.pop())