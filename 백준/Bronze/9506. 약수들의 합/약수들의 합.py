while True:
    n = int(input())
    if n  == -1:
        break
    factor_list = []
    for i in range(n-1):
        if n%(i+1) == 0:
            factor_list.append(i+1)
    if sum(factor_list) == n:
        print(f"{n} = ", end="")
        for i in range(len(factor_list)-1):
            print(f"{factor_list[i]} + ", end="")
        print(f"{factor_list[-1]}")
    else:
        print(f"{n} is NOT perfect.")