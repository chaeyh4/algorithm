import sys

input = sys.stdin.readline

c = int(input().strip())
answer = 0

for _ in range(c):
    line = input().strip()
    count = line.count("for") + line.count("while")
    answer = max(answer, count)

print(answer)