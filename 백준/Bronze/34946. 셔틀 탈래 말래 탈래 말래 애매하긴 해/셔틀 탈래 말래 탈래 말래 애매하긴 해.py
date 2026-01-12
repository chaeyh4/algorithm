import sys

input = sys.stdin.readline

if __name__ == "__main__":
    a,b,c,d = map(int,input().split())
    choice_1 = a+b <= d
    choice_2 = c <= d
    if choice_1 and choice_2:
        print("~.~")
    elif not choice_1 and not choice_2:
        print("T.T")
    elif choice_1 and not choice_2:
        print("Shuttle")
    elif not choice_1 and choice_2:
        print("Walk")