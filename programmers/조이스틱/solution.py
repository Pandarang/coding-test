def solution(name):
    answer = 0
    n = len(name) 
    answer += n - 1

    for c in name :
        up = ord(c) - ord('A') 
        down = ord('Z') - ord(c) + 1
        answer += min(up, down)
    print(answer)
            
    return answer