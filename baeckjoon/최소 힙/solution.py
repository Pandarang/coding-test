import heapq
import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for i in range(n)]
heap = []

for x in arr :
    if x == 0 :
        print(heapq.heappop(heap)) if heap else print(0)
    else :
        heapq.heappush(heap, x)
        