a = input()
stack = []
ans = 0

for i, ch in enumerate(a) :
    if ch == ')' :
        stack.pop() 
        if a[i - 1] == '(' :
            ans += len(stack) 
        else :
            ans += 1

    else :
        stack.append('(') 
print(ans)