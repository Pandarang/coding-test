from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
dist = [-1] * (n + 1)
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque([x])
dist[x] = 0

while q :
    now = q.popleft()
    
    for nx in graph[now] :
        if dist[nx] == -1 :
            dist[nx] = dist[now] + 1
            q.append(nx)

ans = False
for i in range(len(dist)) :
    if dist[i] == k :
        print(i)
        ans = True
if not ans :
    print(-1)