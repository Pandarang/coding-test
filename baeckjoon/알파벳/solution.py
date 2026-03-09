from collections import deque

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

used = [False] * 26
cnt = 1

def dfs(y, x, d) :
    global cnt
    cnt = max(cnt, d)
    
    for i in range(4) :
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m :
            idx = ord(board[ny][nx]) - ord('A')
            if not used[idx] :
                used[idx] = True
                dfs(ny, nx, d + 1)
                used[idx] = False
                
start = ord(board[0][0]) - ord('A')
used[start] = True
dfs(0, 0, 1)

print(cnt)