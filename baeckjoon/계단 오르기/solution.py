n = int(input())

score = [0] * n
for i in range(n) :
    score[i] = int(input())

dp = [0] * n

if n == 1:
    print(score[0])

if n == 2 :
    print(score[0] + score[1])

if n > 2 :
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0] + score[2], score[1] + score[2])

for i in range(3, n) :
    dp[i] = max(
        dp[i-2], dp[i-3] + score[i-1]
    ) + score[i]

print(dp[n-1])