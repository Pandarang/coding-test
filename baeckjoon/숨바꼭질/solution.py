from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def bfs(n, k) :
    visited = [0] * 100001
    q = deque([n]) 
    visited[n] = 1

    while q :
        x = q.popleft()

        if x == k :
            return visited[x] - 1

        for nx in (x-1, x+1, x*2) :
            if 0 <= nx <= 100000 and visited[nx] == 0 :
                visited[nx] = visited[x] + 1
                q.append(nx)

print(bfs(n, k))