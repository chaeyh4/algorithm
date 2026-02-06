import sys

input = sys.stdin.readline

if __name__ == "__main__":
    a, b = map(int,input().rstrip().split())

    ans = a+b
    print(ans)