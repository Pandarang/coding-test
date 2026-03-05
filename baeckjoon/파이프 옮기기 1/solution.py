import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0

def dfs(y, x, d) :
    global ans
    if y == n-1 and x == n-1 :
        ans += 1
        return
    
    if d in (0, 2) :
        nx = x + 1
        if 0 <= nx < n and arr[y][nx] == 0 :
            dfs(y, nx, 0)
    
    if d in (1, 2) :
        ny = y + 1
        if 0 <= ny < n and arr[ny][x] == 0 :
            dfs(ny, x, 1)
        

    ny, nx = y + 1, x + 1
    if 0 <= ny < n and 0 <= nx < n :
        if arr[y][x+1] == 0 and arr[y+1][x] == 0 and arr[y+1][x+1] == 0 :
            dfs(ny, nx, 2)
    
dfs(0, 1, 0)   
print(ans)