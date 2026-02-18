import sys
sys.setrecursionlimit(10**7)

T = int(input())

for _ in range(T) :
    m, n, k = map(int, input().split())
    arr = []
    
    board = [[0] * m for _ in range(n)]
    for _ in range(k) :
        x, y = map(int, input().split())
        board[y][x] = 1

    visited = [[False] * m for _ in range(n)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    def dfs(y, x) :
        visited[y][x] = True
        
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < m and 0 <= ny < n :
                if not visited[ny][nx] and board[ny][nx] == 1 :
                    visited[ny][nx] = True
                    dfs(ny, nx)
        
    cnt = 0
    for y in range(n) :
        for x in range(m) :
            if board[y][x] == 1 and not visited[y][x] :
                dfs(y, x)
                cnt += 1
    print(cnt)