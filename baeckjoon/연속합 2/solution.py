n = int(input())
arr = list(map(int, input().split()))

dp0 = [0] * n
dp1 = [0] * n

dp0[0] = arr[0]
dp1[0] = arr[0]

answer = arr[0]

for i in range(1, n) :
    dp0[i] = max(dp0[i-1] + arr[i], arr[i])
    dp1[i] = max(dp1[i-1] + arr[i], dp0[i-1])

    answer = max(answer, dp0[i], dp1[i])
        
print(answer)