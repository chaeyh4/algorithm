a = int(input())
b = int(input())
c = int(input())

tri_list = [a,b,c]
tri_list.sort()
if sum(tri_list) == 180:
    if tri_list[0] == tri_list[2]:
        print("Equilateral")
    elif tri_list[0] == tri_list[1]:
        print("Isosceles")
    elif tri_list[1] == tri_list[2]:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")