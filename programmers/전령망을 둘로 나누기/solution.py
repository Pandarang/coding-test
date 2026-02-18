from collections import deque

def solution(n, wires):
    m = len(wires)
    graph = [[] for _ in range(n + 1)]
    
    for a, b in wires :
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(start, cur_a, cur_b) :
        visited = [False] * (n + 1)
        q = deque([start])
        visited[start] = True
        cnt = 1
        
        while q : 
            x = q.popleft()
            
            for nx in graph[x] :
                if (x == cur_a and nx == cur_b) or (x == cur_b and nx == cur_a) :
                    continue
                if not visited[nx] :
                    visited[nx] = True
                    q.append(nx)
                    cnt += 1
        return cnt
    
    ans = n
    for a, b in wires :
        cnt = bfs(a, a, b) 
        ans = min(ans, abs(cnt - (n - cnt)))
    
    return ans










