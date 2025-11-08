import sys
input = sys.stdin.readline

n = int(input())
n_set = set(map(int, input().split())) 
m = int(input())
m_list = list(map(int, input().split()))

for x in m_list:
    print(1 if x in n_set else 0)