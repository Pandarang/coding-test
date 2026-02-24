import sys
input = sys.stdin.readline

n = int(input())
T = [0] * (n + 1)
P = [0] * (n + 1)

for i in range(1, n + 1):
    T[i], P[i] = map(int, input().split())

dp = [0] * (n + 2)   

for i in range(n, 0, -1):
    if i + T[i] <= n + 1:
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])
    else:                  
        dp[i] = dp[i + 1]

print(dp[1])