import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().rstrip())
    price = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0, 0, 0] for _ in range(n)]
    dp[0] = price[0]  

    for i in range(1, n):
        dp[i][0] = price[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = price[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = price[i][2] + min(dp[i-1][0], dp[i-1][1])

    print(min(dp[n-1]))  