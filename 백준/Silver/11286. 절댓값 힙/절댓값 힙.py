import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input().rstrip())
    heap = []

    for _ in range(n):
        x = int(input().rstrip())
        if x != 0:
            heapq.heappush(heap, (abs(x), x))  
        else:
            if heap:
                print(heapq.heappop(heap)[1]) 
            else:
                print(0)
