from collections import deque

def solution(maps):
    n = len(maps)      # За
    m = len(maps[0])   # ї­

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                q.append((nx, ny))

    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1
