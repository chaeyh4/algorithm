import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a, b = map(int,input().rstrip().split(","))
        print(a+b)