S = input().strip()

count = [0] * 26

for ch in S:
    count[ord(ch) - ord('a')] += 1

print(' '.join(map(str, count)))