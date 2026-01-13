import sys
input = sys.stdin.readline

n = int(input())
stair_list = [0]
for _ in range(n):
    stair_list.append(int(input()))

dp = [0] * (n + 1)

if n >= 1:
    dp[1] = stair_list[1]
if n >= 2:
    dp[2] = stair_list[1] + stair_list[2]

for i in range(3, n + 1):
    dp[i] = max(
        dp[i-2] + stair_list[i],
        dp[i-3] + stair_list[i-1] + stair_list[i]
    )

print(dp[n])
