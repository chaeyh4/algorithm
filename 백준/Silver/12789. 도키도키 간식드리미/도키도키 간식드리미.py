import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
arr = deque(map(int, input().split()))  
stack = []                               
turn = 1                                  

while arr:
    if arr[0] == turn:
        arr.popleft()
        turn += 1
    else:
        stack.append(arr.popleft())

    while stack and stack[-1] == turn:
        stack.pop()
        turn += 1

while stack and stack[-1] == turn:
    stack.pop()
    turn += 1

print("Nice" if turn == n + 1 else "Sad")