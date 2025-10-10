n = int(input())
for _ in range(n):
    test = list(input())
    cnt = 0
    score = 0
    for i in test:
        if i == "O":
            cnt += 1
            score += cnt
        elif i == "X":
            cnt = 0
            score += cnt
    print(score)