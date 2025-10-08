isbn = list(input().strip())

star_index = isbn.index('*')
sum_val = 0

for i in range(13):
    if i == 12:  
        continue
    if isbn[i] == '*':
        continue
    if i % 2 == 0:
        sum_val += int(isbn[i])
    else:
        sum_val += 3 * int(isbn[i])

m = int(isbn[-1])

weight = 1 if star_index % 2 == 0 else 3

for x in range(10):
    total = sum_val + weight * x + m
    if total % 10 == 0:
        print(x)
        break