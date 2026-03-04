import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().rstrip())
    s = input().rstrip()
    new_s = ''
    for i in s:
        if i.isupper():
            new_s += i.lower()
        else:
            new_s += i.upper()
    print(new_s)
