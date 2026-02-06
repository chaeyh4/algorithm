import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    time_list = []
    for _ in range(n):
        s, e = map(int,input().split())
        time_list.append((s,e))
    time_list.sort(key=lambda x: (x[1], x[0]))
    #print(time_list)
    # 끝나는 시간이 가장 빠른 회의부터 차례때로 정렬

    cnt = 0
    last_end = 0

    for s,e in time_list:
        if s >= last_end:
            cnt += 1
            last_end = e
    print(cnt)