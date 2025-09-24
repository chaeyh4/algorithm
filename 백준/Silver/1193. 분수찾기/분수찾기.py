x = int(input())

n = 0
t = 1
while True:
    n = t*(t+1)/2
    if n>=x:
        if t%2 == 0:
            mother = int(1+n-x)
            son = int(t-(n-x))
        else:
            mother = int(t-(n-x))
            son = int(1+n-x)
        print(str(son)+"/"+str(mother))
        break
    else:
        t += 1