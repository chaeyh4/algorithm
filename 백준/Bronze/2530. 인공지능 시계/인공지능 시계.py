import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
d = int(input())

# 전체 초로 변환
total = a * 3600 + b * 60 + c + d

# 하루는 86400초
total %= 86400

# 다시 시, 분, 초로 변환
new_a = total // 3600
total %= 3600
new_b = total // 60
new_c = total % 60

print(new_a, new_b, new_c)