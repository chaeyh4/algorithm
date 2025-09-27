n, k = map(int, input().split())

factor_list = []

for i in range(n):
    if n%(i+1) == 0:
        factor_list.append(i+1)
if len(factor_list) < k:
    print(0)
else:
    print(factor_list[k-1])