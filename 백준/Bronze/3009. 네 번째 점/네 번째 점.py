a, b = map(int,input().split())
c, d = map(int,input().split())
e, f = map(int,input().split())

list_x = [a,c,e]
list_y = [b,d,f]
list_x.sort()
list_y.sort()

if list_x[0] == list_x[1]:
    g = list_x[2]
else:
    g = list_x[0]

if list_y[0] == list_y[1]:
    h = list_y[2]
else:
    h = list_y[0]

print(g, h)