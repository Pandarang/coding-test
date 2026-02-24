import sys
input = sys.stdin.readline

n = int(input())
MOD = 10007

dp = [1] * 10 

for _ in range(n - 1):
    for j in range(1, 10) :
        dp[j] = (dp[j] + dp[j-1]) % MOD
        
        