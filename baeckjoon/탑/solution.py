from collections import deque

n = int(input())
arr = list(map(int, input().split()))
ans = [0] * n
stack = []

for i, v in enumerate(arr) :
    while stack and stack[-1][1] < v :
        stack.pop()
        
    if stack :
        ans[i] = stack[-1][0] + 1
        
    stack.append((i, v))


print(*ans)