import sys
input = sys.stdin.readline
if __name__ == "__main__":
    n_list = list(map(int,input().rstrip().split()))
    n_list.sort()
    print(n_list[1])
    