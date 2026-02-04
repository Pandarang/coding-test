n, m = map(int, input().split())
maps = []

for _ in range(n) :
    line = input().strip()
    maps.append(list(line))
    
n, m = len(maps), len(maps[0])
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y) :
    visited[x][y] = True
    
    wolf = 0
    sheep = 0
    
    if maps[x][y] == 'o' :
        sheep = 1
    elif maps[x][y] == 'v' :
        wolf = 1

    
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m  :
            if maps[nx][ny] != '#' and not visited[nx][ny] :
                s, w = dfs(nx, ny)
                sheep += s
                wolf += w
    
    return sheep, wolf

sheeps, wolfs = 0, 0

for i in range(n) :
    for j in range(m) :
        if maps[i][j] != '#' and not visited[i][j]:
            s, w = dfs(i, j)
            if s > w:
                sheeps += s
            else:
                wolfs += w

print(sheeps, wolfs)




            

            
        