import sys
input = sys.stdin.readline

s = input().strip()
boom = input().strip()
l = len(boom) 
last = boom[-1]

stack = []

for ch in s :
    stack.append(ch)
    
    if ch == last and len(stack) >= l :
        if ''.join(stack[-l:]) == boom :
            del stack[-l:]
                
ans = ''.join(stack)
print(ans if ans else "FRULA")