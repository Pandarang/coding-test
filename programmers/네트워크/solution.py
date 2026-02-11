from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n) :
        if visited[i] :
            continue
        
        q = deque([i])
        visited[i] = True
        
        while q :
            x = q.popleft()
            for j in range(n) :
                if computers[x][j] == 1 and not visited[j] :
                    visited[j] = True
                    q.append(j)
        answer += 1
    return answer
        