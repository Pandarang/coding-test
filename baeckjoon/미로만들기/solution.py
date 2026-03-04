import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
board = [list(map(int, input().strip())) for _ in range(n)]

INF = 10**9
dist = [[INF] * n for _ in range(n)]
dist[0][0] = 0

q = deque()
q.append((0, 0))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while q :
    y, x = q.popleft()
    
    for i in range(4) :
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n :
            cost = 0 if board[ny][nx] == 1 else 1
            nd = dist[y][x] + cost
            
            if nd < dist[ny][nx] :
                dist[ny][nx] = nd 
                if cost == 0 :
                    q.appendleft((ny, nx))
                else :
                    q.append((ny, nx))

print(dist[n-1][n-1])