from collections import deque

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def bfs(y, x) :
    q = deque()    
    q.append((y, x))
    visited[y][x] = True

    while q :
        y, x = q.popleft()

        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n :
                if not visited[ny][nx] and board[ny][nx] == 1 :
                    visited[ny][nx] = True
                    q.append((ny, nx))

cnt = 0
for y in range(n) :
    for x in range(m) :
        if not visited[y][x] and board[y][x] == 1 :
            bfs(y, x)
            cnt += 1 

print(cnt)