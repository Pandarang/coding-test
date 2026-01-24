s = input()
stack = []
tf = False
result = []

for c in s :
    if c == '<' :
        tf = True
        while stack :
            result.append(stack.pop())
    elif c == '>' :
        tf = False
        result.append(c)
        continue
    
    if tf : 
        result.append(c)
    elif not tf and c == ' ' :
        while stack :
            result.append(stack.pop())
        result.append(c)
    else :
        stack.append(c)
        
while stack :
    result.append(stack.pop())
            
print(''.join(result))