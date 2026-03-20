import heapq

n = int(input())
heap = [int(input()) for _ in range(n)]
heap.sort()
ans = 0

while len(heap) >= 2 :
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    
    ans += x + y
    heapq.heappush(heap, x+y)
    
print(ans)