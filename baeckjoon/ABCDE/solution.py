import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n)]
visited = [False] * n

for a, b in arr :
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, d) :
    if d == 4 :
        print(1)
        sys.exit(0)
        
    visited[x] = True
    
    for nx in graph[x] :
        if not visited[nx] :
            visited[nx] = True
            dfs(nx, d + 1)
    
    visited[x] = False
    
for i in range(n) :
    dfs(i, 0)
        
print(0) 