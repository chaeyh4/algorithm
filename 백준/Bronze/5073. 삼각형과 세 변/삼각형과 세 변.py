while True:
    abc = input()
    if abc == "0 0 0":
        break
    a,b,c = map(int,abc.split())
    abc_list = [a,b,c]
    abc_list.sort()
    if (abc_list[0] + abc_list[1]) > abc_list[2]:
        if abc_list[0] == abc_list[2]:
            print("Equilateral")
        elif abc_list[0] == abc_list[1]:
            print("Isosceles")
        elif abc_list[1] == abc_list[2]:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")