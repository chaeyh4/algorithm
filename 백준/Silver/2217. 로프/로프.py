import sys
input = sys.stdin.readline

if __name__ == "__main__":
    w_list = []
    n = int(input().rstrip())
    for _ in range(n):
        w_list.append(int(input().rstrip()))
    w_list.sort()
    max = 0
    for i in range(n):
        new = w_list[i] * (n-i)
        if max < new: 
            max = new
    print(max)