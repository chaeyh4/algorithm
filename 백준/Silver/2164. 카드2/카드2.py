import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
n_stack = deque()
for i in range(1,n+1):
    n_stack.append(i)

for _ in range(n-1):
    n_stack.popleft()
    n_stack.append(n_stack[0])
    n_stack.popleft()

print(n_stack[0])