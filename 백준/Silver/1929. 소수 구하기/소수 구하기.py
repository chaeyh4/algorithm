import sys
input = sys.stdin.readline

m, n = map(int, input().split())

# 소수 여부를 저장하는 리스트 (True = 소수)
prime = [True] * (n + 1)
prime[0] = prime[1] = False  # 0과 1은 소수가 아님

for i in range(2, int(n**0.5) + 1):
    if prime[i]:
        for j in range(i * i, n + 1, i):
            prime[j] = False

for i in range(m, n + 1):
    if prime[i]:
        print(i)