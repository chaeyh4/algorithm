import sys
input = sys.stdin.readline



def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

if __name__ == "__main__":
    n = int(input())
    factorial_list = reversed(list(str(factorial(n))))
    cnt = 0
    for num in factorial_list:
        if num == "0":
            cnt += 1
        else:
            break
    print(cnt)