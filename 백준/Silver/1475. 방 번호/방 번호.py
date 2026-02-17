import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n_list = list(map(int,input().rstrip()))
    num_cnt = [0]*10

    for n in n_list:
        num_cnt[n] += 1
    
    num_cnt[6] += num_cnt[9]
    six = num_cnt[6]
    if six % 2 != 0:
        num_cnt[6] = six//2 + 1
    else:
        num_cnt[6] = six//2
    num_cnt = num_cnt[:-1]
    print(max(num_cnt))