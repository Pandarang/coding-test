def solution(sizes) :
    answer = 0
    
    weight, height = 0, 0
    n, m = 0, 0
    
    for w, h in sizes :
        weight = max(max(w, h), n)
        height = max(min(w, h), m)

        n = weight
        m = height
    
    return weight * height