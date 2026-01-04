num_list = []

for _ in range(5):
    n = input().strip()
    if n in num_list:
        num_list.remove(n)  
    else:
        num_list.append(n)  

print(num_list[0])