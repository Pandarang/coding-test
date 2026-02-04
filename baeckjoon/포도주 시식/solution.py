n = int(input())

dp = [0] * n

grapes = [int(input()) for i in range(n)]

if n == 1 :
    print(grapes[0])
    exit()
if n == 2 :
    print(grapes[0] + grapes[1])
    exit()
if n > 2 :
    dp[0] = grapes[0]
    dp[1] = grapes[0] + grapes[1]
    dp[2] = max(
        grapes[0] + grapes[1], grapes[0] + grapes[2],grapes[1] + grapes[2]
    )

for i in range(3, n) :
    dp[i] = max(
        dp[i-1],
        dp[i-2] + grapes[i], 
        dp[i-3] + grapes[i-1] + grapes[i]
    ) 
    
print(dp[n-1])
