import sys
input = sys.stdin.readline

if __name__ == "__main__":
    l = int(input())
    if l % 5 == 0:
        print(l//5)
    else:
        print(l//5 + 1)