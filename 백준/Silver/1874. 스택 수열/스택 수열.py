import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []

next_push = 1  

for _ in range(n):
    num = int(input())

    while next_push <= num:
        stack.append(next_push)
        result.append("+")
        next_push += 1

    if stack and stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        sys.exit(0)

print("\n".join(result))