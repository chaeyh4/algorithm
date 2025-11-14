
import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
c = input().rstrip()

if a.isdecimal():
    d = int(a) + 3
    if int(d)%3 != 0 and int(d)%5 != 0:
        print(d)
    elif int(d)%3 == 0 and int(d)%5 != 0:
        print("Fizz")
    elif int(d)%3 != 0 and int(d)%5 == 0:
        print("Buzz")
    elif int(d)%3 == 0 and int(d)%5 == 0:
        print("FizzBuzz")
elif b.isdecimal():
    d = int(b) + 2
    if int(d)%3 != 0 and int(d)%5 != 0:
        print(d)
    elif int(d)%3 == 0 and int(d)%5 != 0:
        print("Fizz")
    elif int(d)%3 != 0 and int(d)%5 == 0:
        print("Buzz")
    elif int(d)%3 == 0 and int(d)%5 == 0:
        print("FizzBuzz")
elif c.isdecimal():
    d = int(c) + 1

    if int(d)%3 != 0 and int(d)%5 != 0:
        print(d)
    elif int(d)%3 == 0 and int(d)%5 != 0:
        print("Fizz")
    elif int(d)%3 != 0 and int(d)%5 == 0:
        print("Buzz")
    elif int(d)%3 == 0 and int(d)%5 == 0:
        print("FizzBuzz")
else:
    print("Fizz")