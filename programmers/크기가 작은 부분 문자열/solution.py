def solution(t, p):
    answer = 0
    nt = len(t)
    np = len(p)
    s = int(p)
    
    for c in range(nt-np+1) :
        if t[c:c+np:1] <= p :
            answer += 1
    
    return answer