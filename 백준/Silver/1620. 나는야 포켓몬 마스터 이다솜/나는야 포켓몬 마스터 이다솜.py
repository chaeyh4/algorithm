import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pokemon_dict = {}
num_dict = {}

for i in range(n):
    pokemon = input().strip()
    pokemon_dict[i+1] = pokemon
    num_dict[pokemon] = i+1

for _ in range(m):
    q = input().strip()
    if q.isdigit():
        print(pokemon_dict[int(q)])
    else:
        print(num_dict[q])