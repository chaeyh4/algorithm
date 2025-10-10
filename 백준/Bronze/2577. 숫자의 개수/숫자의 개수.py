a = int(input())
b = int(input())
c = int(input())

abc = list(str(a*b*c))

cnt = []
for i in range(10):
    cnt_num = 0
    for j in abc:
        if str(i) == j:
            cnt_num += 1
    cnt.append(cnt_num)

for i in cnt:
    print(i)