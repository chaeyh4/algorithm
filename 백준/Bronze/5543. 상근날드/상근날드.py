import sys
input = sys.stdin.readline

burger_list = []
for _ in range(3):
    burger_list.append(int(input()))

drink_list = []
for _ in range(2):
    drink_list.append(int(input()))

print(min(burger_list)+min(drink_list)-50)