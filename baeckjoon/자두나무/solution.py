T, W = map(int, input().split())

arr = [int(input()) for _ in range(T)]

dp = [-10**9] * (W + 1)
dp[0] = 0

for t in range(T) :
    new = dp[:]
    for w in range(W + 1) :
        best = dp[w]
        if w > 0 :
            best = max(best, dp[w - 1])

        pos = 1 if w % 2 == 0 else 2 
        gain = 1 if arr[t] == pos else 0
        new[w] = best + gain
        
    dp = new

print(dp)