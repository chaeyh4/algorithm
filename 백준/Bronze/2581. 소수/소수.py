m = int(input())
n = int(input())
n_list = []
for i in range(m,n+1,1):
    for j in range(2,i+1):
        if i == j:
            n_list.append(i)
        if i%j == 0:
            break
if len(n_list) == 0:
    print(-1)
else:
    print(sum(n_list))
    print(n_list[0])