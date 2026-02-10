import heapq

def solution(s, K):
    answer = 0
    heapq.heapify(s)
    
    while len(s) > 1 :    
        n = heapq.heappop(s)
        if n > K :
            return answer
        elif s and n < K :
            temp = heapq.heappop(s)
            heapq.heappush(s, n + temp * 2)
            answer += 1
    
    if s[0] < K :
        return -1
    return answer