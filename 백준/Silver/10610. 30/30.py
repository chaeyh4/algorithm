import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().rstrip())
    
    n_list = list(map(int,str(n)))
    if 0 not in n_list:
        print(-1)
    else:
        if sum(n_list) % 3 == 0:
            n_list.sort(reverse=True)
            for i in n_list:
                print(i,end="")
        else:
            print(-1)