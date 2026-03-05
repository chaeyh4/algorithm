import sys
input = sys.stdin.readline

if __name__ == "__main__":
    h = [int(input().rstrip()) for _ in range(9)]

    total = sum(h)
    need = total - 100  # 제거해야 하는 두 난쟁이 키 합

    a = b = -1
    found = False

    for i in range(9):
        for j in range(i + 1, 9):
            if h[i] + h[j] == need:
                a, b = i, j
                found = True
                break
        if found:
            break

    ans = [h[k] for k in range(9) if k != a and k != b]
    ans.sort()
    for x in ans:
        print(x)