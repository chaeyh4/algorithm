import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    cnt = 0
    for i in range(1,n+1):        
        num_list = list(str(i))
        #print(num_list)
        if len(num_list) > 1:
            residual = []
            for j in range(len(num_list)-1):
                residual.append(int(num_list[j])-int(num_list[j+1]))
            if len(residual) >= 1 and len(set(residual)) == 1:
                cnt += 1
        else:
            cnt += 1
    print(cnt)