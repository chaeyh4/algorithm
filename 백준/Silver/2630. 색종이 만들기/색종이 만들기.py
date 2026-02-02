import sys

input = sys.stdin.readline

def div(x,y,n):
    color = paper[x][y]
    global white
    global blue
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != paper[i][j]:
                m = n//2
                div(x, y, m) # 색종이 분할 (2사분면)
                div(x, y + m, m) # 색종이 분할 (1사분면)
                div(x + m, y, m) # 색종이 분할 (3사분면)
                div(x + m, y + m, m) # 색종이 분할(4사분면)
                return
    if color == 1:
        blue += 1
    else:
        white += 1
        


    pass

if __name__ == "__main__":
    n = int(input())
    paper = [list(map(int,input().rstrip().split())) for _ in range(n)]
    white, blue = 0,0
    div(0,0,n)
    print(white)
    print(blue)
