n = int(input())
n_list = []

i = 2
while True:
    if n % i == 0:
        n_list.append(i)
        print(i)
        n = n//i
        i = 2
    else:
        i += 1
        if n % i == 0:
            n_list.append(i)
            print(i)
            n = n//i
            i == 2
        if n == i:
            n_list.append(i)
            print(i)
            break
    if n == 1:
        break