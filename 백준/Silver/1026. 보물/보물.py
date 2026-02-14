import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().rstrip())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_sort = sorted(a)  
    b_idx = sorted(range(n), key=lambda i: b[i], reverse=True)

    s = 0
    for k, idx in enumerate(b_idx):
        s += a_sort[k] * b[idx]

    print(s)