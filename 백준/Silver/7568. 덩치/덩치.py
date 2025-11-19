import sys
input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())
    ejdcl_list = []
    rank = []
    for _ in range(n):
        x, y = map(int, input().split())
        ejdcl_list.append((x,y))
    for i in ejdcl_list:
        x = i[0]
        y = i[1]
        cnt = 1
        for j in ejdcl_list:
            if x<j[0] and y<j[1]:
                cnt += 1
        rank.append(cnt)
print(*rank)