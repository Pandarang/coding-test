import sys
input = sys.stdin.readline


def dfs(start) :
    if len(path) == 6 :
        print(*path)
        return
    
    for i in range(start, k) :
        path.append(nums[i])
        dfs(i + 1) 
        path.pop()

while True :
    lotto = input().split()
    if not lotto :
        break
    
    k = int(lotto[0])
    if k == 0 :
        break
    
    nums = list(map(int, lotto[1:]))
    path = []
    dfs(0)
    print()