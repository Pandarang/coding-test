n, m = map(int, input().split())

visited = [False] * (n + 1)
path = []

def dfs(depth) :
    if depth == m :
        print(*path)
        return 
    
    for x in range(1, n + 1) :
        if not visited[x] :
            visited[x] = True
            path.append(x)
            
            dfs(depth + 1)

            path.pop()
            visited[x] = False

dfs(0)
            