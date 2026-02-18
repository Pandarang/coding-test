import sys
input = sys.stdin.readline

C = int(input())
g = [list(map(int, input().split())) for _ in range(2)]

ans = 0

for r in range(2):
    for c in range(C):
        if g[r][c] == 0:
            continue
        
        t = 3
        
        if c > 0 and g[r][c-1] == 1:
            t -= 1
        if c < C-1 and g[r][c+1] == 1:
            t -= 1

        if (r + c) % 2 == 0:  
            if r == 0 and g[1][c] == 1:
                t -= 1
        else:              
            if r == 1 and g[0][c] == 1:
                t -= 1

        ans += t

print(ans)
