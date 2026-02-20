import sys
input = sys.stdin.readline

if __name__ == "__main__":
    babba = [(0, 0) for _ in range(46)]
    babba[0] = (1, 0)
    babba[1] = (0, 1)

    for i in range(2, 46):
        babba[i] = (
            babba[i-1][0] + babba[i-2][0],
            babba[i-1][1] + babba[i-2][1]
        )

    k = int(input().rstrip())
    print(*babba[k])