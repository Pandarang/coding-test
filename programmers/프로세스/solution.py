from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque()
    
    for i, p in enumerate(priorities) :
        q.append((p, i))    

    while q :
        p, i = q.popleft()
        
        if not q or p >= max(x[0] for x in q) :
            answer += 1
            if i == location :
                return answer
        else :
            q.append((p, i))
                