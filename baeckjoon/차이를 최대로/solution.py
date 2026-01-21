n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = []

left = 0
right = len(arr) - 1

while left <= right :
    ans.append(arr[left])
    left += 1
    if left <= right :
        ans.append(arr[right])
        right -= 1
print(ans)