import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

water_q = deque()
hog_q = deque()

for y in range(n) :
    for x in range(m) :
        if arr[y][x] == '*' :
            water_q.append((y, x))
        elif arr[y][x] == 'S' :
            hog_q.append((y, x))
            visited[y][x] = True

time = 0  
while hog_q :
    for _ in range(len(water_q)) :
        y, x = water_q.popleft()
        for i in range(4) :
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m :
                if arr[ny][nx] == '.' :
                    arr[ny][nx] = '*'
                    water_q.append((ny, nx))
    
    for _ in range(len(hog_q)) :
        y, x = hog_q.popleft()
        for i in range(4) :
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny <n and 0 <= nx < m :
                if arr[ny][nx] == 'D' :
                    time += 1
                    print(time)
                    sys.exit(0)
                if arr[ny][nx] == '.' and not visited[ny][nx] :
                    visited[ny][nx] = True
                    hog_q.append((ny, nx))

    time += 1

print("KAKTUS")