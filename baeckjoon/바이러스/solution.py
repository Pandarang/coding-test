n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(1, m + 1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x) :
    visited[x] = True
    cnt = 0

    for nx in graph[x] :
        if not visited[nx] :
            cnt += 1
            cnt += dfs(nx)
    return cnt
ans = dfs(1)
print(ans)