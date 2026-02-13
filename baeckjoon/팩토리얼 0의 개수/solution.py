import sys
input = sys.stdin.readline

m = int(input())

def zeros(n):
    cnt = 0
    while n > 0:
        n //= 5
        cnt += n
    return cnt

left = 0
right = 5*m + 5
ans = -1

while left <= right:
    mid = (left + right) // 2

    if zeros(mid) >= m:
        if zeros(mid) == m:
            ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
