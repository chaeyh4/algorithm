l, p = map(int, input().split())
n = l*p
news = map(int, input().split())
for i in news:
    print(i-n, end=" ")