def solution(sizes):
    answer = 0
    
    n = len(sizes)
    arr = []
    rows = 0
    cols = 0
    
    for r, c in sizes :
        if r >= c :
            arr.append([r, c])
        else :
            arr.append([c, r])
            
    for r, c in arr :
        if r > rows :
            rows = r
        if c > cols :
            cols = c
        
    answer = rows * cols
    
    return answer