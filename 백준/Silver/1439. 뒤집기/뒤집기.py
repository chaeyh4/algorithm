import sys
input = sys.stdin.readline

if __name__ == "__main__":
    s = list(map(int,input().rstrip()))
    cnt = 0 
    len_s = len(s)
    for i in range(1,len_s):
        if s[i] - s[i-1] != 0:
            cnt += 1
    print((cnt+1)//2)


