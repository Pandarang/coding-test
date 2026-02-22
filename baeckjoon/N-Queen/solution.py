n = int(input())

col = [False] * n
dia1 = [False] * (n * 2)
dia2 = [False] * (n * 2)

cnt = 0

def dfs(r) :
    global cnt
    if r == n :
        cnt += 1
        return
    
    for c in range(n) :
        d1 = r + c
        d2 = r - c + n
        if col[c] or dia1[d1] or dia2[d2] :
            continue
        
        col[c] = True
        dia1[d1] = True
        dia2[d2] = True
        
        dfs(r + 1)
        
        col[c] = False
        dia1[d1] = False
        dia2[d2] = False
    
dfs(0)
print(cnt)
    