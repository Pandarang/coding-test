import sys
import heapq

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    m = int(input().strip())
    nums = []
    
    while len(nums) < m :
        nums.extend(map(int, input().split()))
        
    left = []
    right = []
    ans = []
    
    for i, x in enumerate(nums) :
        if not left or x <= -left[0] :
            heapq.heappush(left, -x)
        else :
            heapq.heappush(right, x)
            
        if len(left) < len(right) :
            heapq.heappush(left, -heapq.heappop(right))
        elif len(left) > len(right) + 1 :
            heapq.heappush(right, -heapq.heappop(left))

        if i % 2 == 0 :
            ans.append(-left[0])

    print(len(ans))
    for i in range(0, len(ans), 10) :
        print(*ans[i:i+10])