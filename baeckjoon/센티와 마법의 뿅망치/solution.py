import heapq

N, H, T = map(int, input().split())
arr = [int(input()) for _ in range(N)]

heap = [-x for x in arr]
heapq.heapify(heap)
cnt = 0

for i in range(T) :
    if -heap[0] < H :
        print("YES")
        print(cnt)
        exit()
        
    if -heap[0] > 1 :
        max_val = -heapq.heappop(heap)
        max_val = max_val // 2
        heapq.heappush(heap, -max_val)
        cnt += 1
    else :
        print("NO")
        print(1)
        exit()
        
if -heap[0] < H :
    print("YES")
    print(cnt)
else :
    print("NO")
    print(-heap[0])