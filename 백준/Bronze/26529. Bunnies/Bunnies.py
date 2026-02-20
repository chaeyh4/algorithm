import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().rstrip())
    f = [0]*46
    f[0] = 1
    f[1] = 1
    for i in range(2,46):
        f[i] = f[i-1] + f[i-2]
        #print(i,f[i])
    for _ in range(n):
        i = int(input().rstrip())
        print(f[i])