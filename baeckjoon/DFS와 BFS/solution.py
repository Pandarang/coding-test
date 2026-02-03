from collections import deque

a, b, c = map(int, input().split())

graph1 = [[] for _ in range(a + 1)]
visited1 = [False] * (a + 1)
graph2 = [[] for _ in range(a + 1)]
visited2 = [False] * (a + 1)
arr1, arr2 = [], []

for _ in range(b) :
    x, y = map(int, input().split())
    graph1[x].append(y)
    graph1[y].append(x)
    graph2[x].append(y)
    graph2[y].append(x)

for i in range(1, a+1) :
    graph1[i].sort()
    graph2[i].sort()

def dfs(x) :
    visited1[x] = True
    print(x, end=' ')

    for nxt in graph1[x] :
        if not visited1[nxt] :
            dfs(nxt)

def bfs(start) :
    visited2[start] = True
    q = deque([start])

    while q :
        x = q.popleft()

        for nxt in graph2[x] :
            if not visited2[nxt] :
                visited2[nxt] = True
                q.append(nxt)
                arr2.append(nxt)

dfs(c)
print(*arr1)

arr2.append(c)
bfs(c)
print(*arr2)
