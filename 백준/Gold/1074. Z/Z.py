import sys

# 입력을 빠르게 받기 위해 사용
input = sys.stdin.readline

def solve(n, r, c):
    # Base Case: n이 0이면 (1x1 크기) 더 이상 쪼갤 수 없으므로 0 반환
    if n == 0:
        return 0
    
    # 현재 사분면 한 변 길이의 절반
    half = 2**(n-1)
    
    # 1사분면 (왼쪽 위)
    if r < half and c < half:
        return solve(n-1, r, c)
    
    # 2사분면 (오른쪽 위)
    if r < half and c >= half:
        # 1사분면의 크기(half * half)만큼 이미 숫자가 채워졌다고 가정
        return half * half + solve(n-1, r, c - half)
    
    # 3사분면 (왼쪽 아래)
    if r >= half and c < half:
        # 1, 2사분면 크기만큼 스킵
        return 2 * half * half + solve(n-1, r - half, c)
    
    # 4사분면 (오른쪽 아래)
    else:
        # 1, 2, 3사분면 크기만큼 스킵
        return 3 * half * half + solve(n-1, r - half, c - half)

if __name__ == "__main__":
    n, R, C = map(int, input().split())
    # 리스트를 만들지 않고 바로 계산 결과 출력
    print(solve(n, R, C))