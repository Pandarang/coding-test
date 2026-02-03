n = int(input())
signs = input().split()

def ok(prev, x, sign) :
    return (prev < x) if sign == '<' else (prev > x)
    
    
def solve(candidates) :
    visited = [False] * 10
    path = []
    
    def dfs(depth) :
        if depth == n+1 :
            return True
        
        for x in candidates :
            if visited[x] :
                continue
            if depth > 0 and not ok(path[-1], x, signs[depth-1]) :
                continue
            
            visited[x] = True
            path.append(x)
            if dfs(depth + 1) :
                return True
            path.pop()
            visited[x] = False

        return False
    
    dfs(0)
    return ''.join(map(str, path))

mx = solve(range(9, -1, -1))
mn = solve(range(10))

print(mx)
print(mn)