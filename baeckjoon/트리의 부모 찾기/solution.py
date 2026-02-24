import sys
sys.setrecursionlimit(10**6)

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n-1)]
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for x, y in arr :
    graph[x].append(y)
    graph[y].append(x)

stack = [1]
visited[1] = True
parent = [0] * (n + 1)

while stack :
    x = stack.pop()
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = True
            parent[nx] = x
            stack.append(nx)

for i in range(2, n + 1):
    print(parent[i])