# 백준 26004번: HI-ARC=?
# 문자열에서 H, I, A, R, C 의 개수를 세고,
# 그중 최솟값이 만들 수 있는 "HIARC"의 개수이다.

import sys

input = sys.stdin.readline

n = int(input().strip())
s = input().strip()

targets = "HIARC"
counts = [s.count(ch) for ch in targets]

print(min(counts))