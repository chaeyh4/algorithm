import sys
input = sys.stdin.readline

num = ['0','1','2','3','4','5','6','7','8','9']

if __name__ == "__main__":
    equation = input().rstrip()
    equation_list = []
    tmp = ''

    for ch in equation:
        if ch in num:
            tmp += ch
        else:
            equation_list.append(tmp)
            equation_list.append(ch)
            tmp = ''
    equation_list.append(tmp)

    i = 0
    while i < len(equation_list):
        if equation_list[i] == '+':
            num1 = int(equation_list[i-1])
            num2 = int(equation_list[i+1])
            new = num1 + num2

            # i-1, i, i+1 제거
            equation_list.pop(i-1)
            equation_list.pop(i-1)
            equation_list.pop(i-1)

            # 결과 삽입
            equation_list.insert(i-1, str(new))

            # i를 줄여서 다시 검사
            i -= 1
        else:
            i += 1

    i = 0
    while i < len(equation_list):
        if equation_list[i] == '-':
            num1 = int(equation_list[i-1])
            num2 = int(equation_list[i+1])
            new = num1 - num2

            equation_list.pop(i-1)
            equation_list.pop(i-1)
            equation_list.pop(i-1)
            equation_list.insert(i-1, str(new))

            i -= 1
        else:
            i += 1

    print(equation_list[0])