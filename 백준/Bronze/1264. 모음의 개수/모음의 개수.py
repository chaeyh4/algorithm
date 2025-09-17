while True:
    sen = list(input())
    cnt = 0
    ahdma = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if '#' in sen:
        break
    for i in sen:
        for j in ahdma:
            if i == j:
                cnt += 1
    print(cnt)