n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()

left = 1
right = arr[-1]
answer = 0

while left <= right :
    mid = (left + right) // 2
    
    cnt = 1
    last = arr[0]
    
    for i in range(1, n) :
        if arr[i] - last >= mid :
            cnt += 1
            last = arr[i]
        
    if cnt >= m :
        answer = mid
        left = mid + 1
    else :
        right = mid - 1

print(answer)