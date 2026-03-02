import sys
from itertools import permutations

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().rstrip())
    nums = list(range(1, n + 1))

    out = []
    for p in permutations(nums):
        out.append(" ".join(map(str, p)))
    sys.stdout.write("\n".join(out))