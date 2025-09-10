a,b,c = map(int, input().split())
list_abc = [a,b,c]
a,b,c = sorted(list_abc)

award = 0
if a == b == c :
    award = 10000 + a * 1000
elif a == b or b==c or a==c:
    award = 1000 + (b*100)
else:
    award = c * 100

print(award)