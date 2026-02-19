from collections import deque

def one_diff(a, b) :
    diff = 0
    for x, y in zip(a, b) :
        if x != y :
            diff += 1
            if diff > 1 :
                return False
    return diff == 1

def solution(begin, target, words):
    answer = 0
    
    if not target in words :
        return 0
    
    n = len(words)
    visited = [False] * n
    q = deque([(begin, 0)])

    while q :
        cur, dist = q.popleft()
        if cur == target :
            return dist
        
        for i in range(n) :
            if not visited[i] and one_diff(cur, words[i]) :
                visited[i] = True
                q.append((words[i], dist + 1))
    
    return 0








