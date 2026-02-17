import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().rstrip())
    rest = 1000 - n
    cnt = 0
    money = [500,100,50,10,5,1]

    for m in money:
        cnt += rest//m
        rest %= m
        #print(rest)
    print(cnt)