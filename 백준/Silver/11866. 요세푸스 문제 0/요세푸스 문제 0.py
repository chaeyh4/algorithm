import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int,input().split())
    circle = deque(range(1,n+1))
    print("<", end="")
    while len(circle) > 1:
        for i in range(k-1):
            circle.append(circle[i])
        for i in range(k-1):
            circle.popleft()
        print(circle[0], end = ", ")
        circle.popleft()
    print(f"{circle[0]}>")