import sys
input = sys.stdin.readline

if __name__ == "__main__":
    a = int(input())
    w, v = map(int,input().rstrip().split())
    if w/v >= a:
        print(1)
    else:
        print(0)