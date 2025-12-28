import sys
input = sys.stdin.readline

if __name__ == "__main__":
    a, b = map(int,input().rstrip().split())
    c, d = map(int,input().rstrip().split())
    if a+c > b+d:
        print("Yongdap")
    elif a+c < b+d:
        print("Hanyang Univ.")
    else:
        print("Either")