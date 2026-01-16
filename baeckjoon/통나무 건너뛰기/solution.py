from collections import deque

n = int(input())
arr = []


for _ in range(n) :
    ans = deque()
    minN = 0
    int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
        
    for x in range(len(arr)) :
        if x % 2 == 0 :
            ans.append(arr[x])
        else :
            ans.appendleft(arr[x])

    for x in range(len(ans) - 1) :
        temp = abs(ans[x] - ans[x+1])
        if temp > minN :
            minN = temp
        
    print(minN)
