import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int,input().rstrip().split())
    print((n*m)-1)