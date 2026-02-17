import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().rstrip())
    for i in range(n,0,-1):
        star = "*"*(i*2-1)
        blank = " "*(n-i)
        print(blank+star)
    for i in range(2,n+1):
        star = "*"*(i*2-1)
        blank = " "*(n-i)
        print(blank+star)