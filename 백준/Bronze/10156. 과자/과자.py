import sys

input = sys.stdin.readline

if __name__ == "__main__":
    k,n,m = map(int,input().rstrip().split())
    diff =  m - (k*n)
    if diff >= 0:
        print(0)
    else:
        print(-diff)