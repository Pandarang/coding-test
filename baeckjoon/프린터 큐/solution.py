from collections import deque

t = int(input())

for _ in range(t) :
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    st = []
    q = deque()
    for i, v in enumerate(arr) :
        q.append((v, i))

    cnt = 0
    while q :
        b, a = q.popleft()
        
        if q and max(q, key=lambda x: x[0])[0] > b :
            q.append((b, a))
            continue
            
        cnt += 1
        if a == m :
            print(cnt)
            break
    