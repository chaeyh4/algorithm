import sys

def last_computer(a: int, b: int) -> int:
    a %= 10
    if a == 0:
        return 10

    # a의 일의 자리 패턴(주기)을 직접 미리 정의
    cycles = {
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1],
    }

    cycle = cycles[a]
    idx = (b - 1) % len(cycle)
    return cycle[idx]

def main():
    input = sys.stdin.readline
    t = int(input().strip())
    out = []
    for _ in range(t):
        a, b = map(int, input().split())
        out.append(str(last_computer(a, b)))
    print("\n".join(out))

if __name__ == "__main__":
    main()