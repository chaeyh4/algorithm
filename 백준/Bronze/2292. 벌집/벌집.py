n = int(input())
x = 0
while True:
    sum = 1+x*(12+(x-1)*6)/2
    if sum>=n:
        print(x+1)
        break
    else:
        x+=1