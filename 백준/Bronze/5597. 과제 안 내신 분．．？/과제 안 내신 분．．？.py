arr1 = []
for i in range(30):
    arr1.append(int(i)+1)


arr2 = []
for i in range(28):
    n = input()
    arr2.append(int(n))


arr3 = list(set(arr1)-set(arr2))
arr3.sort()

print(arr3[0])
print(arr3[1])