n, m = map(int, input().split())

emeqh_list = []

for _ in range(n):
    emeqh = input()
    emeqh_list.append(emeqh)

qhaht_list = []
for _ in range(m):
    qhaht = input()
    qhaht_list.append(qhaht)

emeqhaht = sorted(list(set(emeqh_list) & set(qhaht_list)))

print(len(emeqhaht))
for i in emeqhaht:
    print(i)