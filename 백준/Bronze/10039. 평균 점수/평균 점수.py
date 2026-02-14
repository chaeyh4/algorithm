import sys

input = sys.stdin.readline

if __name__ == "__main__":
    sum = 0
    for _ in range(5):
        n = int(input().rstrip())
        if n < 40:
            sum += 40
        else:
            sum += n
    print(sum//5)