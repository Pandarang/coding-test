def solution(numbers):
    answer = ''
    arr = []
    
    for n in numbers :
        arr.append(str(n))

    arr.sort(key=lambda x: x[0], reverse=True)

    print(arr)
        
    
    return answer