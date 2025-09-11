n = int(input())
arr = input().split()

arr_list = []

for i in range(n):
    arr_list.append(int(arr[i]))

print(min(arr_list), max(arr_list))