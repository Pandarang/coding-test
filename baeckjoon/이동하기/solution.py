n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
dp = [row[:] for row in arr]

for y in range(n) :
    for x in range(m) :
        if y == 0 and x == 0 :
            continue
        best = 0
        if y > 0 :
            best = max(best, dp[y-1][x])
        if x > 0 :
            best = max(best, dp[y][x-1])
        if x > 0 and y > 0 :
            best = max(best, dp[y-1][x-1])
        dp[y][x] = best + arr[y][x]        
            
print(dp[n-1][m-1])