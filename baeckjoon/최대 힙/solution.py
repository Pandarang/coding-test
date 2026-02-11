import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n) :
    x = int(input())

    if not heap and x == 0 :
        print(0)
    elif x == 0 :
        print(-heapq.heappop(heap))
    else :
        heapq.heappush(heap, -x)    
