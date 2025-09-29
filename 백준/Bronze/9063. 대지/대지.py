n = int(input())
x_list = []
y_list = []

for i in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)
x_min = min(x_list)
x_max = max(x_list)
y_min = min(y_list)
y_max = max(y_list)

print((y_max-y_min)*(x_max-x_min))