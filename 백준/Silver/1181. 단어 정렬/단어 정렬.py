n = int(input())
word_list = []
for i in range(n):
    word = input()
    if word not in word_list:
        word_list.append(word)
word_list.sort(key=lambda x: (len(x), x))
for i in word_list:
    print(i)