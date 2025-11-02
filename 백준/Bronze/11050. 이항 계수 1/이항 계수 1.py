import sys

input = sys.stdin.readline

N, K = map(int, input().split())

def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

answer = factorial(N) // (factorial(N-K) * factorial(K))
print(answer)