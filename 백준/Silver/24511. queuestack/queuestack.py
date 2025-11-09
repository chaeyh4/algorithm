import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
types = list(map(int, input().split()))  
inits = list(map(int, input().split()))
m = int(input())
queries = list(map(int, input().split()))

pipe = deque([inits[i] for i in range(n) if types[i] == 0])

out = []
for x in queries:
    pipe.appendleft(x)
    out.append(pipe.pop())

print(*out)