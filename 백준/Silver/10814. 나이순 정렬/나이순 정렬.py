n = int(input())

mem_list = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    mem_list.append([age,name])

mem_list.sort(key= lambda x: x[0])
for i in range(n):
    print(mem_list[i][0], mem_list[i][1])