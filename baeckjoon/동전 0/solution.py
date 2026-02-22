n, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]

cnt = 0
for coin in reversed(arr) :
    if k == 0 :
        break
    cnt += k // coin
    k %= coin

print(cnt)