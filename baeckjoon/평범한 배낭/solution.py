n, k = map(int, input().split())

arr = []

for _ in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))
    
dp = [0] * (k + 1)


for w, v in arr :
    for weight in range(k, w-1, -1) :
        dp[weight] = max(dp[weight], dp[weight-w]+v)

print(dp[k])
