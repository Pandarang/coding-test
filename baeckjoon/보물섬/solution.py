from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(y, x) :
    dist = [[-1] * m for _ in range(n)]
    dist[y][x] = 0
    
    q = deque([(y, x)])
    
    while q :
        y, x = q.popleft()
        
        for i in range(4) :
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m :
                if dist[ny][nx] == -1 and board[ny][nx] == 'L' :
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))

    return max(map(max, dist))

answer = 0
visited = [[False] * m for _ in range(n)]
for y in range(n) :
    for x in range(m) :
        if not visited[y][x] and board[y][x] == 'L' :
            answer = max(answer, bfs(y, x))

print(answer)