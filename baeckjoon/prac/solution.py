from collections import deque

T = int(input())

for _ in range(T) :
    n, m= map(int, input().split())
    arr = list(map(int, input().split()))

    q = deque()
    for i, k in enumerate(arr) :
        q.append((k, i))
    
    cnt = 0
    
    while q  :
        p, i = q.popleft()
        
        if q and p < max(x[0] for x in q) :
            q.append((p, i))
        else :
            cnt += 1
            if i == m :
                print(cnt)
                break