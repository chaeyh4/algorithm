import sys
input = sys.stdin.readline

if __name__ == "__main__":
    text = input()
    n = len(text)


    for i in range(n//10):
        print(text[i*10:(i*10)+10])
    print(text[(n//10)*10:])