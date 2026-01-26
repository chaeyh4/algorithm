import sys

input = sys.stdin.readline
MOD = 10007

if __name__ == "__main__":
    n = int(input())
    dp = [0] * (n+1)
    dp[1] = 1
    if n == 1:
        print(dp[n])
    else:
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = (dp[i-1] + dp[i-2])%MOD
        print(dp[n])