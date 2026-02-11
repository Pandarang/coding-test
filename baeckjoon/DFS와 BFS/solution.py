from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

for _ in range(m) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, n+1) :
    graph[i].sort() 

def dfs(x) :
    visited[x] = True
    print(x, end=" ")
    
    for nx in graph[x] : 
        if not visited[nx] :
            dfs(nx)


def bfs(start) :
    q = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True

    while q :
        x = q.popleft()
        print(x, end=' ')
        
        for nx in graph[x] :
            if not visited[nx] :
                visited[nx] = True
                q.append(nx)

dfs(v)
print()
bfs(v)