n, k = map(int,input().split())

coin_list = []

for _ in range(n):
    coin = int(input())
    coin_list.append(coin)

cnt = 0
for i in range(-1, -n-1, -1):
    cnt += k // coin_list[i]
    k %= coin_list[i]
    if k == 0:
        break
print(cnt) 