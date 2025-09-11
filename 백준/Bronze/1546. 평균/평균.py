n = int(input())
arr = input().split()
arr_list = []
for i in arr:
    arr_list.append(int(i))

m = max(arr_list)

new_arr_list = []
for i in arr_list:
    new = i / m * 100
    new_arr_list.append(new)

print(sum(new_arr_list)/n)