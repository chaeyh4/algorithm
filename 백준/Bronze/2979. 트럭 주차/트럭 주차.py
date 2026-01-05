A, B, C = map(int, input().split())

time = [0] * 101  # 각 시간대에 주차된 트럭 수

for _ in range(3):
    start, end = map(int, input().split())
    for t in range(start, end):
        time[t] += 1

cost = 0
for t in range(1, 101):
    if time[t] == 1:
        cost += A
    elif time[t] == 2:
        cost += 2 * B
    elif time[t] == 3:
        cost += 3 * C

print(cost)