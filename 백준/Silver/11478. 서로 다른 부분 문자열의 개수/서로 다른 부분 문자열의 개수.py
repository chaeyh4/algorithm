import sys
input = sys.stdin.readline
s = input().strip()
s_list = []

for i in range(len(s)):
    for j in range(len(s)):
        s_list.append(s[i:j+1])

print(len(set(s_list))-1)