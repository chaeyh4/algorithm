n = int(input())

ok = True
for i in range(1,1000001):
    qnsgo = list(str(i))
    sum = i
    for j in qnsgo:
        sum += int(j)
    if sum == n:
        print(i)
        ok = False
        break
if ok == True:
    print(0)