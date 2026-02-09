import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 0, max(trees)
answer = 0

while left <= right :
    mid = (left + right) // 2
    wood = 0
    
    for h in trees :
        if h > mid :
            wood += h - mid
    
    if wood >= m :
        answer = mid
        left = mid + 1
    else :
        right = mid - 1

print(answer)