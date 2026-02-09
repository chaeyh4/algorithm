import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().rstrip())
    heap = []
    for _ in range(n):
        x = int(input().rstrip())
        if x > 0:
            heapq.heappush(heap,x*-1)
        else:
            if heap:
                result = heapq.heappop(heap)
                print(result*-1)
            else:
                print(0)
