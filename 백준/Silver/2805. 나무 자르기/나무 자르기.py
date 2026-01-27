import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))

    lo, hi = 0, max(trees)
    ans = 0
    trees_local = trees  

    while lo <= hi:
        mid = (lo + hi) // 2

        wood = 0

        for h in trees_local:
            if h > mid:
                wood += h - mid
                if wood >= m:
                    break

        if wood >= m:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    print(ans)

if __name__ == "__main__":
    main()
