def solution(array, commands):
    answer = []
    stack = []
    
    for (a, b, c) in commands :
        stack.append(array[a-1:b])
        stack[0].sort()
        answer.append(stack[0][c-1])
        stack.pop()
    
    return answer