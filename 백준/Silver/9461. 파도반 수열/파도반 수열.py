import sys
input = sys.stdin.readline

t = int(input())
test_list = [int(input()) for _ in range(t)]

max_n = max(test_list)

num_list = [1, 1, 1, 2, 2]

for i in range(5, max_n):
    num_list.append(num_list[i-1] + num_list[i-5])

for n in test_list:
    print(num_list[n-1])