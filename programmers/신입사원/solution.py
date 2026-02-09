import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()
    
    cnt = 1
    temp = arr[0][1]
    for i in range(1, len(arr)) :
        if temp > arr[i][1] :
            temp = arr[i][1]
            cnt += 1

    print(cnt)