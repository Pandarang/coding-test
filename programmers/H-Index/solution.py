def solution(citations):
    answer = 0
    n = len(citations)
    
    citations.sort(key=lambda x: -x)    

    for idx, i in enumerate(citations) :
        if i >= idx + 1 :
            answer = idx + 1
    
    return answer
