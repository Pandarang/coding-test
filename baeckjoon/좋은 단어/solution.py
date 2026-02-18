n = int(input())
answer = 0

for _ in range(n) :
    arr = list(input())
    stack = []
    cnt = 1

    for i in arr :
        if stack and stack[-1] == i :
            stack.pop()
        else :
            stack.append(i)
    
    if not stack :
        answer += 1
        
print(answer)
        
        