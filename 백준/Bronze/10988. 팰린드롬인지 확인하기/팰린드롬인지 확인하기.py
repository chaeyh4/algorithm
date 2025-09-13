n = input()

list_n = list(n)

list_n_ori = list_n.copy()
list_n.reverse()

if list_n == list_n_ori:
    print(1)
else:
    print(0)