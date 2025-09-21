while True:
    n = input()
    if n == "# 0 0":
        break
    a, b, c = n.split()
    if int(b) > 17 or int(c) >= 80:
        print(a, "Senior")
    else:
        print(a, "Junior")