n = int(input())
arr = list(map(int, input().split()))

ans = []

for i in range(n, 0, -1) :
    ans.insert(arr[i-1], i)

print(*ans)