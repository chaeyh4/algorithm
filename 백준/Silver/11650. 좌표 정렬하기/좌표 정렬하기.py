n = int(input())

xy_list = []

for i in range(n):
    x, y = map(int, input().split())
    xy_list.append([x,y])

xy_list.sort(key=lambda x:(x[0],x[1]))

for i in range(n):
    print(xy_list[i][0], xy_list[i][1])