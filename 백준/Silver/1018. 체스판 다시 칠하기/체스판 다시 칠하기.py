n, m = map(int,input().split())

board = []

for i in range(n):
    line = list(input())
    board.append(line)

case1 = list("WBWBWBWB")
case2 = list("BWBWBWBW")

board1 = []
for i in range(4):
    board1.append(case1)
    board1.append(case2)
board2 = []
for i in range(4):
    board2.append(case2)
    board2.append(case1)


wrong = 64

for i in range(n-8+1):
    for j in range(m-8+1):
        cnt = 0
        for k in range(8):
            for l in range(8):
                if board1[k][l] != board[i+k][j+l]:
                    cnt += 1
        if cnt <= wrong:
            wrong = cnt


for i in range(n-8+1):
    for j in range(m-8+1):
        cnt = 0
        for k in range(8):
            for l in range(8):
                if board2[k][l] != board[i+k][j+l]:
                    cnt += 1
        if cnt <= wrong:
            wrong = cnt
print(wrong)