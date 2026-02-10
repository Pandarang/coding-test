def solution(participant, completion):
    dic = {}
    
    for d in participant :
        dic[d] = dic.get(d, 0) + 1
    
    for d in completion :
        dic[d] -= 1
    
    for k, v in dic.items() :
        if v > 0 :
            return k
