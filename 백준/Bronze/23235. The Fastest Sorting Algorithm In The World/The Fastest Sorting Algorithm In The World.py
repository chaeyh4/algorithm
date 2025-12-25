import sys

data = sys.stdin.read().split()
i = 0
case = 1

while True:
    n = int(data[i]); i += 1
    if n == 0:
        break
    i += n  # 숫자 n개 스킵
    print(f"Case {case}: Sorting... done!")
    case += 1