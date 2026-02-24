n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
s = 0 
left = 0

for right in range(n) :
    s += arr[right]

    while s > m :
        s -= arr[left]
        left += 1
        
    if s == m :
        count += 1
        
print(count)