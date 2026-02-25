import heapq
import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort()

heap = []

for s, t in arr :
    if heap and heap[0] <= s :
        heapq.heappop(heap)
    heapq.heappush(heap, t)
    
print(len(heap))