import sys
n = int(input())
num_list = []
for i in range(n):
    num = int(sys.stdin.readline())
    num_list.append(num)

num_list = sorted(num_list)

for i in range(n):
    print(num_list[i])