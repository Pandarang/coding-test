n, m, l = map(int, input().split())
arr = list(map(int, input().split())) if n > 0 else []
arr.sort()
d = 0

arr = [0] + arr + [l]
left, right = 1, l
ans = l

while left <= right :
    mid = (left + right) // 2
    cnt = 0
    
    for i in range(1, len(arr)) :
        d = arr[i] - arr[i-1]
        cnt += (d - 1) // mid
        
    if cnt <= m :
        ans = mid
        right = mid - 1
    else :
        left = mid + 1

print(ans)