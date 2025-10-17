n = int(input())

size_list = list(map(int,input().split()))

t, p = map(int, input().split())

cnt = 0
for i in size_list:
    if i % t != 0:
        cnt += i // t + 1
    else:
        cnt += i // t

print(cnt)
print(n//p, n%p)