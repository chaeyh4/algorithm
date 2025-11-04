import sys
input = sys.stdin.readline

n = int(input())

n_f = 1
for i in range(2,n+1):
    n_f *= i

print(n_f)