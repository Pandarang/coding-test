import sys
input = sys.stdin.readline

r, c = map(int, input().split())

arr = [input() for _ in range(r)]
visited = [[False] * c for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y) :
    visited[y][x] = True
    wolfs = 0
    sheeps = 0

    if arr[y][x] == 'v' :
        wolfs += 1
    elif arr[y][x] == 'o' :
        sheeps += 1

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < c and 0 <= ny < r : 
            if not visited[ny][nx] and arr[ny][nx] != '#' :
                s, w = dfs(nx, ny)
                sheeps += s
                wolfs += w
    return sheeps, wolfs

total_sheeps = 0
total_wolfs = 0

for y in range(r) :
    for x in range(c) :
        if not visited[y][x] and arr[y][x] != '#' :
            s, w = dfs(x, y)
            if s > w :
                total_sheeps += s
            else :
                total_wolfs += w

print(total_sheeps, total_wolfs)
