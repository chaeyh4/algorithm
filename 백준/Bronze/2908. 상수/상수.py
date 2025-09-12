a, b = input().split()
a = list(a)
b = list(b)
a.reverse()
b.reverse()

rev_a = int(a[0]+a[1]+a[2])
rev_b = int(b[0]+b[1]+b[2])

if rev_a > rev_b:
    print(rev_a)
else:
    print(rev_b)