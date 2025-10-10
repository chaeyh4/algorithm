n = int(input())

n_list = list(map(int, input().split()))

n_list.sort()

cal = 0
for i in range(n):
    cal += sum(n_list[:i+1])
print(cal)