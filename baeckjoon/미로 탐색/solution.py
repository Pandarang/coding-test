from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]


dist = [[0] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
q.append((0, 0))
dist[0][0] = 1

while q :
    x, y = q.popleft()

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m :
            if maze[nx][ny] == 1 and dist[nx][ny] == 0 :
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

print(dist[n-1][m-1])