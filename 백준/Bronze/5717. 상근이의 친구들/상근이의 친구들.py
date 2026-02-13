import sys
input = sys.stdin.readline

if __name__ == "__main__":
    while True:
        m,f = map(int,input().rstrip().split())
        if m == 0 and f == 0 :
            break
        print(m+f)