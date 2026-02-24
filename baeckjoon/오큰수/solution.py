n = int(input())
arr = list(map(int, input().split()))

ans = [-1] * n
stack = []


for i in range(n-1, -1, -1) :
    v = arr[i]
    while stack and stack[-1] <= v :
        stack.pop()
    ans[i] = stack[-1] if stack else -1
    stack.append(v)
    
print(*ans)