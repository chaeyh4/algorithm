import sys
input = sys.stdin.readline

n = int(input())

# 바텀업으로 F(n) 계산
f = [0] * (n + 2)   # n=1,2 대비
f[1] = 1
f[2] = 1

cnt2 = 0
for i in range(3, n + 1):
    f[i] = f[i - 1] + f[i - 2]
    cnt2 += 1        # 반복문 수행 횟수

cnt1 = f[n]          # 재귀 기저호출 횟수와 동일

print(cnt1, cnt2)