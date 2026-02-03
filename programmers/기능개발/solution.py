from collections import deque

def solution(p, speeds):
    answer = []
    arr = []
    time = 0
    
    for i in range(len(p)) :
        need = 100 - p[i]
        time = (need + speeds[i]- 1) // speeds[i]
        arr.append(time)
    
    cur = arr[0]
    cnt = 1
    for a in arr[1:] :
        if cur < a :
            answer.append(cnt)
            cnt = 1
            cur = a
        else :
            cnt += 1
    answer.append(cnt)
    
    return answer