import sys
input = sys.stdin.readline
if __name__ == "__main__":
    c = int(input())
    for _ in range(c):
        n_list = list(map(int,input().split()))
        mean = sum(n_list[1:])/n_list[0]
        cnt = 0
        for i in n_list[1:]:
            if i > mean:
                cnt += 1
        result = round(cnt/n_list[0]*100,3)
        print(f"{result:.3f}%")