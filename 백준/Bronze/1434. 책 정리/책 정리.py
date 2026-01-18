import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int,input().rstrip().split())
    a_list = list(map(int,input().rstrip().split()))
    b_list = list(map(int,input().rstrip().split()))

    for b in b_list:
        for idx, a in enumerate(a_list):
            if b <= a:
                #print(a,b)
                new_a = a-b
                a_list[idx] = new_a
                break
            else:
                continue
        #print(a_list)
    print(sum(a_list))