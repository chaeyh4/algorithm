n = 9

arr = []
max_row = []
for i in range(n):
	row = list(map(int, input().split()))    
	arr.append(row)
	max_row.append(max(row))

max_value = max(max_row)

max_row_index = max_row.index(max(max_row))
print(max_value)
print(max_row_index+1, arr[max_row_index].index(max_value)+1)