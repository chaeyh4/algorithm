import sys 
from collections import Counter
if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    n_list = []
    for _ in range(n):
        n_list.append(int(input()))
    n_list.sort()
    print(int(round(sum(n_list)/n,0)))
    print(n_list[((n+1)//2)-1])
    count_n = Counter(n_list)
    max_count = max(list(Counter(n_list).values()))
    max_count_num = []
    for i in n_list:
        if count_n[i] == max_count:
            if i not in max_count_num:
                max_count_num.append(i)
    if len(max_count_num) == 1:
        print(max_count_num[0])
    else:
        print(max_count_num[1])
    print(n_list[-1] - n_list[0])