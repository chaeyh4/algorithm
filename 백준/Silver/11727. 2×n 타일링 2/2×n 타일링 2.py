import sys

def main():
    input = sys.stdin.readline
    n = int(input().strip())
    MOD = 10007

    if n == 1:
        print(1)
        return
    if n == 2:
        print(3)
        return

    a, b = 1, 3  # dp[1], dp[2]
    for _ in range(3, n + 1):
        a, b = b, (b + 2 * a) % MOD
    print(b)

if __name__ == "__main__":
    main()