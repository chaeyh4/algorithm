s = input().strip()
k = input().strip()

filtered = ''.join(ch for ch in s if not ch.isdigit())

print(1 if k in filtered else 0)