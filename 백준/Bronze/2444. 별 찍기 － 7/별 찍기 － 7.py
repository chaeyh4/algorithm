n = int(input())

for i in range(n):
    space = n-1-i
    print(" "*space+"*"*(i*2+1))

for i in range(n-1):
    space = i+1
    print(" "*space+"*"*(2*(n-1-i)-1))