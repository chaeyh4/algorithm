import sys
input = sys.stdin.readline

n = int(input())
time_list = list(map(int, input().split()))

y = 0  # 영식 요금
m = 0  # 민식 요금

for t in time_list:
    y += (t // 30 + 1) * 10
    m += (t // 60 + 1) * 15

if y < m:
    print("Y", y)
elif y > m:
    print("M", m)
else:
    print("Y M", y)