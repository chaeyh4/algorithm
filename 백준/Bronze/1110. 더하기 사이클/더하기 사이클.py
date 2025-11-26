import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n = input().strip()
    if int(n) < 10:
        n = "0" + n

    original_num = n
    cnt = 0

    while True:
        # 각 자리 숫자 더하기
        a = int(n[0])
        b = int(n[1])
        s = a + b

        # 새로운 n을 만들기
        n = n[1] + str(s % 10)
        cnt += 1

        # 사이클이 원래 수로 돌아오면 종료
        if n == original_num:
            print(cnt)
            break