a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

ok = True
for i in (n0, 10000): 
    fn = a1 * i + a0
    if fn > c * i:     
        ok = False
        break

print(1 if ok else 0)