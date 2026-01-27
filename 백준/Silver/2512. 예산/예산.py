import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().strip())
    req = list(map(int,input().strip().split()))
    m = int(input().strip())

    lo = 0
    hi = max(req)
    ans = 0
    money_range = [lo,hi]

    while (lo<=hi):
        mid = (lo+hi)//2
        total = 0
        #print(lo,hi)
        for r in req:
            total += mid if r>=mid else r

            
        #print(sum)
        if total <= m:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
        
    print(ans)
        

            