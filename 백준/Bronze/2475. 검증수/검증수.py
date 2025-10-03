num_list = list(map(int,input().split()))

sum = 0
for i in num_list:
    sum += i**2
print(sum%10)