

def dfs(start) :
    if len(path) == 6 :
        print(*path)
        return
        
    for i in range(start, k) :
        path.append(arr[i])
        dfs(i + 1)
        path.pop()
    
while True :
    n = list(map(int, input().split()))
    if not n :
        break
    
    k = n[0]
    if k == 0 :
        break
    
    arr = n[1:]
    path = []
    
    dfs(0)
    print()