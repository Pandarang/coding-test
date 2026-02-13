import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

l = 0
r = len(arr) - 1
max_num = float('inf')
ans_l, ans_r = arr[l], arr[r]

while l < r :
    s = arr[l] + arr[r]
    abs_s = abs(s)

    if abs_s < max_num :
        max_num = abs_s
        ans_l, ans_r = arr[l], arr[r]
        if max_num == 0 :
            break
    
    if s < 0 :
        l += 1
    else :
        r -= 1

print(ans_l, ans_r)