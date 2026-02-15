def solution(p, c):
    dic = {}
    answer = []
    
    for x in p :
        dic[x] = dic.get(x, 0) + 1
    
    for x in c :
        dic[x] -= 1
    
    for k in dic :
        if dic[k] > 0 :
            answer.append(k)
    
    return ''.join(answer)