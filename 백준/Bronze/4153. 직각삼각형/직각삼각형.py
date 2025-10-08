while True:
    abc = input()
    if abc == "0 0 0":
        break
    abc_list = list(map(int,abc.split()))
    abc_list.sort()
    if abc_list[2]**2 == abc_list[0]**2 + abc_list[1]**2:
        print("right")
    else:
        print("wrong")