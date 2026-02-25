import heapq

n = int(input())
heap = [int(input()) for _ in range(n)]

heapq.heapify(heap) 
ans = 0

while len(heap) >= 2 :
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    tmp = a + b
    
    heapq.heappush(heap, tmp)
    ans += tmp
    
print(ans)

    