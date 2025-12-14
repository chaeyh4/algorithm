import sys
input = sys.stdin.readline

if __name__ == "__main__":
    r1, s = map(int, input().rstrip().split())
    r2 = (2*s)-r1
    print(r2)