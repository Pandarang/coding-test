n, k = map(int, input().split())
MOD = 1000000000

dp = [[0] * (n + 1) for _ in range(k + 1)]

for y in range(1, k + 1) :
    dp[y][0] = 1
for x in range(0, n + 1) :
    dp[1][x] = 1


for y in range(2, k + 1) :
    for x in range(1, n + 1) :
        dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % MOD

print(dp[k][n])


