import sys
input = sys.stdin.readline

n = int(input())

company_set = set()
for _ in range(n):
    name, log = input().split()
    if log == "enter":
        company_set.add(name)
    if log == "leave":
        company_set.remove(name)

company_list = list(company_set)
company_list.sort(reverse=True)

for c in company_list:
    print(c)