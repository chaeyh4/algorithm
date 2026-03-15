import sys

s = sys.stdin.readline().strip()

if s == "0":
    print(0)
else:
    table = ['000', '001', '010', '011', '100', '101', '110', '111']

    result = [bin(int(s[0]))[2:]]  # 첫 자리는 앞의 0 제거
    for ch in s[1:]:
        result.append(table[int(ch)])

    print(''.join(result))