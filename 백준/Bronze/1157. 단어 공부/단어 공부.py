n = input()
n = n.upper()
list_n = list(n)
count_n = []
for i in set(list_n):
    count_n.append(list_n.count(i))

max_count = max(count_n)
cnt = 0
for i in count_n:
    if i == max_count:
        cnt += 1
if cnt > 1:
    print("?")
else:
    print(list(set(list_n))[count_n.index(max(count_n))])