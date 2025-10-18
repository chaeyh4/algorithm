import sys
input = sys.stdin.readline

n = int(input())
n_set = set(map(int, input().split())) 

m = int(input())
m_list = list(map(int, input().split()))

for m in m_list:
    if m in n_set:   
        print(1, end=' ')
    else:
        print(0, end=' ')