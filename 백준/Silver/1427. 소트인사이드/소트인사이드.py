n = list(input())
num_list = []
for i in n:
    num_list.append(int(i))
    
num_list.sort(reverse=True)
for i in num_list:
    print(i, end="")