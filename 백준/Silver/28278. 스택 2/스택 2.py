import sys
input = sys.stdin.readline
n = int(input())

x_stack = []
for _ in range(n):
    x = input().strip().split()
    if x[0] == "1":
        x_stack.append(int(x[1]))
    elif x[0] == "2":
        if len(x_stack) == 0:
            print(-1)
        else:
            print(x_stack.pop())
    elif x[0] == "3":
        print(len(x_stack))
    elif x[0] == "4":
        if len(x_stack) == 0:
            print(1)
        else:
            print(0)
    elif x[0] == "5":
        if len(x_stack) == 0:
            print(-1)
        else:
            print(int(x_stack[-1]))