def solution(arr):
    answer = []
    stack = []
    
    answer.append(arr[0])
    for i in arr :
        if stack and stack[-1] != i :
            answer.append(i)
        stack.append(i)
        
    
    return answer