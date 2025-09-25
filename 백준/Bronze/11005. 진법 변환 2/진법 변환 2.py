N, B = map(int, input().split())

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = []

while N > 0:
    result.append(digits[N % B])
    N //= B

print("".join(reversed(result)))