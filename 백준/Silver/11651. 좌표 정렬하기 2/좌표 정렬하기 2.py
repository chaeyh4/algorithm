import sys
n = int(sys.stdin.readline())

xy_list = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    xy_list.append([x,y])

xy_list.sort(key=lambda x:(x[1],x[0]))

for i in range(n):
    print(xy_list[i][0], xy_list[i][1])