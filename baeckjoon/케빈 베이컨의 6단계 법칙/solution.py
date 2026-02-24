from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(1, m + 1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start) :
    dist = [-1] * (n + 1)   
    q = deque([start])
    dist[start] = 0
    while q :
        x = q.popleft()
        
        for nx in graph[x] :
            if dist[nx] == -1 :
                dist[nx] = dist[x] + 1
                q.append(nx)
    return sum(dist[1:])

answer = []
for i in range(1, n + 1):
    answer.append((bfs(i), i))      

answer.sort()                       
print(answer[0][1])