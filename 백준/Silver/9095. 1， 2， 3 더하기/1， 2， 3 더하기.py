t = int(input())

num_list = [1,2,4]

for i in range(3,11):
    total = num_list[i-3]+num_list[i-2]+num_list[i-1]
    num_list.append(total)

for _ in range(t):
    n = int(input())
    print(num_list[n-1])