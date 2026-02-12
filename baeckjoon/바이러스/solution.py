n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)


for _ in range(m) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(x) :
    visited[x] = True
    cnt = 0
    
    for nx in graph[x] :
        if not visited[nx] :
            cnt += 1
            dfs(nx)
    return cnt

print(dfs(1))
