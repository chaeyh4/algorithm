import sys
input = sys.stdin.readline

if __name__ == "__main__":
    num = input()
    num_list = list(num)
    if "7"  in num_list:
        if int(num) % 7 == 0:
            print(3)
        else:
            print(2)
    else:
        if int(num) % 7 == 0:
            print(1)
        else:
            print(0)