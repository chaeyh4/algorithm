import sys
input = sys.stdin.readline

def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    sum = fibo(num-1) + fibo(num-2)
    return sum

if __name__ == "__main__":
    n = int(input())
    print(fibo(n))