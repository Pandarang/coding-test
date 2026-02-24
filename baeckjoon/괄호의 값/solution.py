arr = list(input())

stack = []
answer = 0
cnt = 1


for i, ch in enumerate(arr) :
    if ch == '(' :
        stack.append(ch)
        cnt *= 2
    elif ch == '[':
        stack.append(ch)
        cnt *= 3
    elif ch == ')' :
        if not stack or stack[-1] != '(' :
            print(0)
            break
        if arr[i-1] == '(' :
            answer += cnt
        stack.pop()
        cnt //= 2
    elif ch == ']':
        if not stack or stack[-1] != '[':
            print(0)
            break
        if arr[i-1] == '[':
            answer += cnt
        stack.pop()
        cnt //= 3
else :
    print(0 if stack else answer)