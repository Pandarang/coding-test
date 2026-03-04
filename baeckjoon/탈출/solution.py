import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

grid = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

water_q = deque()
hop_q = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for y in range(n) :
    for x in range(m) :
        if grid[y][x] == '*' :
            water_q.append((y, x))
        elif grid[y][x] == 'S' :
            hop_q.append((y, x)) 
            visited[y][x] = True
            
time = 0

while hop_q :
    for _ in range(len(water_q)) :
        y, x = water_q.popleft()
        for i in range(4) :
            ny, nx = y + dy[i], x + dx[i] 
            if 0 <= ny < n and 0 <= nx < m :
                if grid[ny][nx] == '.' :
                    grid[ny][nx] = '*' 
                    water_q.append((ny, nx))
    
    for _ in range(len(hop_q)) :
        y, x = hop_q.popleft()
        for i in range(4) :
            ny, nx = y + dy[i], x + dx[i] 
            if 0 <= ny < n and 0 <= nx < m :
                if grid[ny][nx] == 'D' :
                    print(time + 1)
                    sys.exit(0)
                if grid[ny][nx] == '.' and not visited[ny][nx] :
                    visited[ny][nx] = True
                    hop_q.append((ny, nx)) 
    
    time +=1

print("KAKTUS")