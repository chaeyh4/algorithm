n = int(input())

x_list = list(map(int,input().split()))

x_list_sorted = sorted(set(x_list))
    

compress_dict = {value: idx for idx, value in enumerate(x_list_sorted)}

for i in x_list:
    print(compress_dict[i], end=' ')