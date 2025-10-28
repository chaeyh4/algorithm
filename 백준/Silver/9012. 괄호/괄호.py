t = int(input())

for _ in range(t):
    ps = input().strip()
    stack = []
    valid = True

    for ch in ps:
        if ch == '(':
            stack.append(ch)
        else:  # ch == ')'
            if stack:
                stack.pop()
            else:
                valid = False
                break

    if valid and not stack:
        print("YES")
    else:
        print("NO")