n = int(input())
MOD = 9901

dp = [[0] * 3 for _ in range(n+1)]

dp[0][0] = 1
dp[0][1] = 1
dp[0][2] = 1

for i in range(1, n+1) :
    dp[i][0] = sum(dp[i-1]) % MOD
    dp[i][1] = dp[i-1][0] + dp[i-1][2] % MOD
    dp[i][2] = dp[i-1][0] + dp[i-1][1] % MOD
    
print(sum(dp[n-1]) % MOD)