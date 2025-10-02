# Baekjoon 19532: 수학은 비대면강의입니다
a, b, c, d, e, f = map(int, input().split())

det = a*e - b*d              # Δ ≠ 0 (문제에서 유일해 보장)
x = (c*e - b*f) // det
y = (a*f - c*d) // det

print(x, y)