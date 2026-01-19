import sys
input = sys.stdin.readline

if __name__ == "__main__":
    x = int(input())
    stick_list = [64]
    #cnt = 0
    while True:
        #print(stick_list)
        if sum(stick_list) == x:
            print(len(stick_list))
            break
        if sum(stick_list)>x:
            stick_list.sort()
            min_stick = stick_list[0]
            divide_min_stick = min_stick/2
            stick_list.append(divide_min_stick)
            stick_list.append(divide_min_stick)
            stick_list.pop(0)
            if sum(stick_list) - divide_min_stick >= x:
                stick_list.pop(-1)