import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    heap = []
    for _ in range(n):
        x = int(input().rstrip())
        
        if x > 0:
            heapq.heappush(heap,x)
            #print(heap)
        elif x == 0:
            if not heap:
                print(0)
            else:
                result = heapq.heappop(heap)
                print(result)