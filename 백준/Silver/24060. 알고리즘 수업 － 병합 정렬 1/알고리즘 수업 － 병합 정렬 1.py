import sys
input = sys.stdin.readline
sys.setrecursionlimit(1_000_000)

cnt = 0
ans = -1

def merge_sort(A, p, r, k_num):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q, k_num)
        merge_sort(A, q + 1, r, k_num)
        merge(A, p, q, r, k_num)

def merge(A, p, q, r, k_num):
    global cnt, ans
    i, j = p, q + 1
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i]); i += 1
        else:
            tmp.append(A[j]); j += 1
    while i <= q:
        tmp.append(A[i]); i += 1
    while j <= r:
        tmp.append(A[j]); j += 1

    t = 0
    for k in range(p, r + 1):
        A[k] = tmp[t]
        cnt += 1
        if cnt == k_num and ans == -1:   
            ans = A[k]
        t += 1

if __name__ == "__main__":
    a_size, k_num = map(int, input().split())
    a_list = list(map(int, input().split()))
    merge_sort(a_list, 0, a_size - 1, k_num)
    print(ans)