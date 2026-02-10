def solution(nums):
    answer = 0
    
    n = len(nums) // 2
    t = set(nums)
    m = len(t)

    if n >= m :
        answer = m
    else :
        answer = n
    
    return answer

