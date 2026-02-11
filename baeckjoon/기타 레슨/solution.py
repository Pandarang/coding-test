n, m = map(int, input().split())
arr = list(map(int, input().split()))

left, right = max(arr), sum(arr)

while left <= right :
    mid = (left + right) // 2
    total = 0
    cnt = 1
    
    for x in arr :
        if total + x > mid :
            cnt += 1
            total = 0
        total += x
        
    if cnt <= m :
        ans = mid 
        right = mid - 1
    else :
        left = mid + 1
        
print(ans) 
    