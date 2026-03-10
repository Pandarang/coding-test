n, m = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

def dfs(idx, total) :
    global answer
    if idx == n :
        if total == m :
            answer += 1
        return
            
    dfs(idx + 1, total + arr[idx])
    dfs(idx + 1, total)

dfs(0, 0)

if m == 0 :
    answer -= 1
    
print(answer)