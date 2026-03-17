from collections import deque

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, a, b = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

virus = []
for i in range(n) :
    for j in range(n) :
        if board[i][j] != 0 :
            virus.append((board[i][j], 0, i, j))

virus.sort()
q = deque(virus)

while q :
    num, t, y, x = q.popleft()
    
    if t == s :
        break
    
    for i in range(4) :
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < n :
            if board[ny][nx] == 0 :
                board[ny][nx] = num
                q.append((board[ny][nx], t+1, ny, nx))

print(board[a-1][b-1])