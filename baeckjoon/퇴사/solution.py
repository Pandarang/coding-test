n = int(input())

t = [0] * (n + 1)
p = [0] * (n + 1)

for i in range(1, n + 1) :
    t[i], p[i] = map(int, input().split())
    
dp = [0] * (n + 2)

for i in range(n, 0, - 1) :
    end = i + t[i]
    if end <= n + 1 :
        dp[i] = max(dp[i + 1], p[i] + dp[end])
    else :
        dp[i] = dp[i + 1]

print(dp[1])