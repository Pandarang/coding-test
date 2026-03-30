n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[1])
stack = []

for k, v in arr :
    if not stack or stack[-1][1] <= k :
        stack.append((k, v))

print(len(stack))