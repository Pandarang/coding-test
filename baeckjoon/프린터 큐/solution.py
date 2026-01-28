from collections import deque
n = int(input())
temp = 0

for _ in range(n) :
    a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    
    q = deque([(arr[i], i) for i in range(a)])
    cnt = 0
    
    while q :
        p, idx = q.popleft()
        
        if q :
            max_arr = max(x[0] for x in q)
        else :
            max_arr = 0
            
        if p < max_arr :
            q.append((p, idx))
        else :
            cnt += 1
            if idx == b :
                print(cnt)
                break
            
        