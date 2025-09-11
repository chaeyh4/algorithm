import sys
n = int(sys.stdin.readline().rstrip("\n"))
for i in range(n):
    a, b = map(int,sys.stdin.readline().rstrip("\n").split())
    print(a+b)