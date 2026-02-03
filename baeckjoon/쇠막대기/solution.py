s = input()
stack = []
count = 0

for i in range(len(s)) :
    if s[i] == ')' :
        stack.pop()
        if s[i-1] == '(' :
            count += len(stack)
        else :
            count += 1
    else :
        stack.append(s[i])

print(count)