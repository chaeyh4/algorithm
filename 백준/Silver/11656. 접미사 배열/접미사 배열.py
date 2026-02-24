import sys
input = sys.stdin.readline

if __name__ == "__main__":
    s = input().rstrip()
    suffix = []
    len_s = len(s)
    for i in range(len_s):
        suffix.append(s[i:])
    suffix.sort()
    for s in suffix:
        print(s)