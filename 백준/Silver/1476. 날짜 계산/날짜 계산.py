import sys
input = sys.stdin.readline

if __name__ == "__main__":
    e, s, m = map(int,input().rstrip().split())
    e %= 15
    s %= 28
    m %= 19
    y = 1
    while True:
        if y%15 == e:
            if y%28 == s:
                if y%19 == m:
                    print(y)
                    break
                else:
                    y += 1
            else:
                y += 1
        else:
            y += 1