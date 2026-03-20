from itertools import combinations
import sys

n = int(input())
board = [list(input().split()) for _ in range(n)]

tmp = []
T = []
for y in range(n) :
    for x in range(n) :
        if board[y][x] == 'X' :
            tmp.append((y, x))
        elif board[y][x] == 'T' :
            T.append((y, x))

dy, dx = [0, 0, 1, -1], [1, -1, 0, 0]

for a, b, c in combinations(tmp, 3) :
    board[a[0]][a[1]] = 'O'
    board[b[0]][b[1]] = 'O'
    board[c[0]][c[1]] = 'O'    

    answer = False
    for ty, tx in T :
        for i in range(4) :
            ny, nx = ty + dy[i], tx + dx[i]
            while 0 <= ny < n and 0 <= nx < n :
                if board[ny][nx] == 'S' :
                    answer = True
                    break
                if board[ny][nx] == 'O' :
                    break
                
                ny += dy[i]
                nx += dx[i]
    if not answer :
        print("YES")
        sys.exit()
        
    board[a[0]][a[1]] = 'X'
    board[b[0]][b[1]] = 'X'
    board[c[0]][c[1]] = 'X'   
    

        
        
print("NO")
                
        
        
        
        
        
        
        
        
        
        