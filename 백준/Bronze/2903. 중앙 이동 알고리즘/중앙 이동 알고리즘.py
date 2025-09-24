initial = 2
n = int(input())
for i in range(n):
	initial = (initial-1+initial)
print(initial*initial)