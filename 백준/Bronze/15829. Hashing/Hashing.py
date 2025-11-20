import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    string_list = list(input().rstrip())
    num_list = []
    for l in string_list:
        num_list.append(ord(l)-96)
    hash = 0
    for i, n in enumerate(num_list):
        hash += n * (31**i)
    print(hash % 1234567891)