n = int(input())

left, right = 1, 
answer = 0

while left <= right :
    mid = (left + right) // 2
    cnt = 0
    temp = 1

    for i in range(1, mid) :
        temp *= i
        print(temp)
    s = str(temp)


    for c in reversed(temp) :
        if c == '0' :
            cnt += 1
        else :
    
    if cnt <= n :
        answer = mid
        left = mid + 1
    else :
        right = mid - 1
    
print(answer)



    
