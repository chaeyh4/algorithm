n = int(input())

for i in range(n):
   star = "*"*(2*(i+1)-1)
   space = " "*(n-i-1)
   #print(len(space))
   print(space+star) 