from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)] 
visited = [False] * (n+1)

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

def bfs(start) :
    global cnt
    q = deque([start])
    visited[start] = True

    while q :
        x = q.popleft()

        for nxt in graph[x] :
            if not visited[nxt] :
                cnt += 1
                visited[nxt] = True
                q.append(nxt)

bfs(1)
print(cnt)
