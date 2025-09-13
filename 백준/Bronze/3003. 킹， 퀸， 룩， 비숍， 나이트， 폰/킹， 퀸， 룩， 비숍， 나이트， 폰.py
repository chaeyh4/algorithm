chess = [1,1,2,2,2,8]

k,q,l,b,n,p = map(int,input().split())
list_white = [k,q,l,b,n,p]

for i in range(6):
    ans = chess[i]-list_white[i]
    print(ans, end=" ")