from collections import deque

T = int(input())

for _ in range(T) :
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    q = deque()
    q.append(arr.pop())
    
    while arr :
        if arr :
            q.append(arr.pop())
        if arr :
            q.appendleft(arr.pop())
            
    max_num = 0
    for i in range(1, len(q)) :
        max_num = max(q[i] - q[i-1], max_num)

    print(max_num)