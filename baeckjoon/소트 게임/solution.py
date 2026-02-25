from collections import deque

n, k = map(int, input().split())
arr = list(input().split())

start = ''.join(arr)
target = ''.join(sorted(arr)) 

q = deque([(start, 0)])
visited = {start}

while q :
    cur, d = q.popleft()
    
    if cur == target :
        print(d)
        exit()
    
    for i in range(n-k+1) :
        nxt = cur[:i] + cur[i:i+k][::-1] + cur[i+k:]
        
        if nxt not in visited :
            visited.add(nxt)
            q.append((nxt, d+1))
print(-1)