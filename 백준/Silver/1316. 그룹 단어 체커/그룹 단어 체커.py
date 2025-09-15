n = int(input())
cnt = 0
for i in range(n):
    word = input()
    word_alpha = list(set(word))
    word_result = 0
    for j in word_alpha:
        word_idx = []
        for idx, value in enumerate(word):
            if j == value:
                word_idx.append(idx)
        if len(word_idx) >1:
            word_idx_diff = []
            for k in range(len(word_idx)-1):
                word_idx_diff.append(word_idx[k+1]-word_idx[k])
            if sum(word_idx_diff) == len(word_idx)-1:
                word_result += 0
            else:
                word_result += 1
    if word_result == 0:
        cnt +=1

print(cnt)