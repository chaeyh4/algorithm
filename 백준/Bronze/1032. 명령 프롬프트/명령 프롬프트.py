import sys

n = int(sys.stdin.readline().strip())
files = [sys.stdin.readline().strip() for _ in range(n)]

L = len(files[0])
ans = []

for i in range(L):
    ch = files[0][i]
    if all(f[i] == ch for f in files):
        ans.append(ch)
    else:
        ans.append('?')

print(''.join(ans))