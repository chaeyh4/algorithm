a, b, v = map(int, input().split())
day = 0
if (v-a)%(a-b) != 0:
    day +=1

day += (v-a)//(a-b)
day += 1

print(day)