check = [False] * 10001   

def d(n):
    return n + sum(map(int, str(n)))

for i in range(1, 10001):
    dn = d(i)
    if dn <= 10000:
        check[dn] = True   

for i in range(1, 10001):
    if not check[i]:
        print(i)