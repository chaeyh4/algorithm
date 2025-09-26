while True:
    case = input()
    if case == "0 0":
        break
    a, b = map(int, case.split())
    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")