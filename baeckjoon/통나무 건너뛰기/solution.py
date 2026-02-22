import sys
from collections import deque

input = sys.stdin.readline


T = int(input())

for _ in range(T) :
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    q = deque()
    q.append(arr.pop())
    
    while arr :
        q.append(arr.pop())
        if arr :
            q.appendleft(arr.pop())
            
    max_num = 0
    for i in range(1, n) :
        max_num = max(abs(q[i] - q[i-1]), max_num)
        
    max_num = max(abs(q[-1] - q[0]), max_num)
    print(max_num)