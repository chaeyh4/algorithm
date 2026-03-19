s = input().strip()

stack = []
answer = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if s[i - 1] == '(':   # 레이저
            answer += len(stack)
        else:                 # 막대의 끝
            answer += 1

print(answer)