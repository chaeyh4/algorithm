import sys
input = sys.stdin.readline

if __name__ == "__main__":
    s = int(input().rstrip())
    sum = 0
    cnt = 1
    while True:
        sum += cnt
        if sum>s:
            print(cnt-1)
            break
        else:
            cnt +=1
            #print(sum)