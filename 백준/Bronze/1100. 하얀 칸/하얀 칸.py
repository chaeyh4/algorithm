import sys

input = sys.stdin.readline

if __name__ == "__main__":
    board = [list(input().strip()) for i in range(8)]
    #print(board)
    cnt = 0
    for i in range(0,8,2):
        for j in range(0,8,2):
            if board[i][j] == "F":
                cnt += 1
                #print(i, j)
    for i in range(1,8,2):
        for j in range(1,8,2):
            #print(i, j)
            if board[i][j] == "F":
                cnt += 1
                
    
    print(cnt)
