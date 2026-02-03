def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    visited = [False] * n

    def dfs(cur_k, cnt) :
        nonlocal answer
        answer = max(answer, cnt)
        
        for i in range(n) :
            need, cost = dungeons[i]
            if not visited[i] and cur_k >= need :
                visited[i] = True
                dfs(cur_k - cost, cnt + 1)
                visited[i] = False
        
    dfs(k, 0)
    return answer
