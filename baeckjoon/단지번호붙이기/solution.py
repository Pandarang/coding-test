from collections import deque

n = int(input())

board = [list(map(int, input())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

def bfs(y, x) :
    q = deque([(y, x)])
    visited[y][x] = True
    cnt = 1
    
    while q :
        y, x = q.popleft()
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n :
                if not visited[ny][nx] and board[ny][nx] == 1 :
                    visited[ny][nx] = True
                    cnt += 1
                    q.append((ny, nx))
    return cnt
answer = 0
ans = []
for y in range(n) :
    for x in range(n) :
        if not visited[y][x] and board[y][x] == 1 :
            answer += 1
            ans.append(bfs(y, x))

print(answer)
ans.sort()
for i in ans :
    print(i)