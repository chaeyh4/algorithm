import sys
input = sys.stdin.readline

n_dict = {}
n = int(input())

for i in list(map(int,input().split())):
    if i in n_dict.keys():
        n_dict[i] += 1
    else:
        n_dict[i] = 1


m = int(input())
for i in list(map(int,input().split())):
    if i in n_dict.keys():
        print(n_dict[i], end = " ")
    else:
        print(0, end = " ")