n = int(input())
m = int(input())
arr = list(map(int, input().split()))

arr.sort()

l = 0
r = len(arr) - 1
cnt = 0

while l < r :
    if arr[l] + arr[r] == m :
        l += 1
        r -= 1
        cnt += 1
    elif arr[l] + arr[r] < m :
        l += 1
    else :
        r -= 1

print(cnt)