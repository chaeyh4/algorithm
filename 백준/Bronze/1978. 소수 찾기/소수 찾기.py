n = int(input())
n_list = list(map(int,input().split()))
thtn = 0
for i in range(n):
    check_num = n_list[i]
    cnt = 0
    for j in range(check_num):
        if check_num % (j+1) == 0:
            cnt += 1
    if cnt == 2:
        thtn += 1
print(thtn)