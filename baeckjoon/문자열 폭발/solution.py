import sys
input = sys.stdin.readline

s = input().strip()
boom = input().strip()

stack = []
length = len(boom)

for ch in s :
    stack.append(ch)
    
    if len(stack) >= length and ''.join(stack[-length:]) == boom :
        del stack[-length:]
    
res = ''.join(stack)

if res :
    print(res)
else :
    print("FRULA")