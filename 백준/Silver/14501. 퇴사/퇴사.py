import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().rstrip())
    t = [0] * n
    p = [0] * n
    for i in range(n):
        t[i], p[i] = map(int, input().split())

    dp = [0] * (n + 1)  # dp[n] = 0 (퇴사일 이후)

    for i in range(n - 1, -1, -1):
        if i + t[i] <= n:
            dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
        else:
            dp[i] = dp[i + 1]

    print(dp[0])