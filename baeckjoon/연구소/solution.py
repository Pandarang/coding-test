from collections import deque
from itertools import combinations

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(y, x) :
    visited[y][x] = True
    q = deque([(y, x)])
    cnt = 1
    while q :
        y, x = q.popleft()
        
        for i in range(4) :
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m :
                if not visited[ny][nx] and board[ny][nx] == 0 :
                    visited[ny][nx] = True
                    cnt += 1
                    q.append((ny, nx))
    return cnt

def bfs_2(y, x) :
    visited[y][x] = True
    q = deque([(y, x)])

    while q :
        y, x = q.popleft()
        
        for i in range(4) :
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m :
                if not visited[ny][nx] and board[ny][nx] == 0 :
                    visited[ny][nx] = True
                    board[ny][nx] = 2
                    q.append((ny, nx))

tmp = []
for y in range(n) :
    for x in range(m) :
        if board[y][x] == 0 :
            tmp.append((y, x))

answer = 0
for a, b, c in combinations(tmp, 3) :
    board[a[0]][a[1]] = 1
    board[b[0]][b[1]] = 1
    board[c[0]][c[1]] = 1
    visited = [[False] * m for _ in range(n)]
    res = 0
    
    for y in range(n) :
        for x in range(m) :
            if not visited[y][x] and board[y][x] == 2 :
                bfs_2(y, x)
    
    for y in range(n) :
        for x in range(m) :
            if not visited[y][x] and board[y][x] == 0 :
                res += bfs(y, x)
    
    answer = max(answer, res)
    
    board[a[0]][a[1]] = 0
    board[b[0]][b[1]] = 0
    board[c[0]][c[1]] = 0

print(answer)