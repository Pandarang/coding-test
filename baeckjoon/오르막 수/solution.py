n = int(input())
MOD = 10007

dp = [1] * 10

for _ in range(2, n + 1) :
    for j in range(1, 10) :
        dp[j] += (dp[j] - dp[j-1]) / MOD 
print(dp)

# dp[1] 0123456789
n = 2
# 1 123456789
# 2 23456789 