k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

left, right = 1, max(arr)
answer = 0

while left <= right :
    mid = (left + right) // 2
    cnt = 0
    
    for x in arr :
        if x >= mid :
            cnt += x // mid
            
    if cnt >= n :
        answer = mid 
        left = mid + 1
    else :
        right = mid - 1
        
print(answer)
