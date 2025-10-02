import itertools
n, m = map(int, input().split())

num_list  = list(map(int, input().split()))

it = itertools.combinations(num_list, 3)

sum_list = []

for i in list(it):
    sum_list.append(sum(i))

sum_list.sort()


ok = True
for i in range(len(sum_list)):
    if sum_list[i] == m:
        print(m)
        ok = False
        break
    elif sum_list[i] > m:
        print(sum_list[i-1])
        ok = False
        break
if ok == True:
    print(sum_list[-1])