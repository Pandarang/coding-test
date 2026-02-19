import sys
sys.setrecursionlimit(10**6)

n = int(input())

arr = [input().strip() for _ in range(n)]
arr2 = [list(row) for row in arr]

for y in range(n) :
    for x in range(n) :
        if arr2[y][x] == "R" :
            arr2[y][x] = "G"

visited = [[False] * n for _ in range(n)] 
visit = [[False] * n for _ in range(n)] 

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def dfs(y, x) :
    visited[y][x] = True
    s = arr[y][x]
    
    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= ny < n and 0 <= nx < n :
            if not visited[ny][nx] and arr[ny][nx] == s :
                visited[ny][nx] = True
                dfs(ny, nx)
    return s

def dfs2(y, x) :
    visit[y][x] = True
    s = arr2[y][x]
    
    for i in range(4) :
        ny = y + dy[i]
        nx = x + dx[i]
        
        if 0 <= ny < n and 0 <= nx < n :
            if not visit[ny][nx] and arr2[ny][nx] == s :
                visit[ny][nx] = True
                dfs2(ny, nx)
    return s

answer1 = 0
answer2 = 0
for y in range(n) :
    for x in range(n) :
        if not visited[y][x] :
            answer1 += 1
            dfs(y, x)
        if not visit[y][x] :
            answer2 += 1
            dfs2(y, x)
            

print(answer1, end=" ")
print(answer2)