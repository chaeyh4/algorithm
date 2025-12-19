import sys
input = sys.stdin.readline

if __name__ == "__main__":
    a, b = map(int,input().rstrip().split())
    print(b-a, b)