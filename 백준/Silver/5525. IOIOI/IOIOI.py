import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().rstrip())
    m = int(input().rstrip())
    s = input().rstrip()

    cnt = 0
    k = 0      # 연속으로 발견한 "IOI" 덩어리 개수
    i = 1

    while i < m - 1:
        if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
            k += 1
            if k == n:
                cnt += 1
                k -= 1   # 겹치는 패턴을 위해 1개 남겨둠
            i += 2       # "IOI"면 다음은 그 뒤의 I부터 보는 게 이득
        else:
            k = 0
            i += 1

    print(cnt)
