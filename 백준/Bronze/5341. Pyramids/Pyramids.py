import sys
input = sys.stdin.readline

if __name__ == "__main__":
    while True:
        n = int(input().rstrip())
        if n == 0:
            break
        cnt = 0
        for i in range(n+1):
            cnt += i
        print(cnt)