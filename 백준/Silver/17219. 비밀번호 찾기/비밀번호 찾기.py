n, m = map(int,input().split())

pass_dict = {}

for _ in range(n):
    site, password = input().split()
    pass_dict[site] = password

password = []
for _ in range(m):
    find_site = input()
    password.append(pass_dict[find_site])

for i in password:
    print(i)