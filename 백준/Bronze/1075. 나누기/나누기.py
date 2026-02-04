n = int(input().strip())
f = int(input().strip())

# N의 뒤 두 자리를 00으로 만들기
base = (n // 100) * 100

# base부터 +99까지 순회하면서 나누어지는 수 찾기
for i in range(100):
    if (base + i) % f == 0:
        # 뒤 두 자리만 출력 (두 자리 수 형식 유지)
        print(f"{i:02d}")
        break
