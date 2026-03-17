n = int(input())
arr = list(map(int, input().split()))
four = list(map(int, input().split()))

max_ans = -int(1e9)
min_ans = int(1e9)
def dfs(idx, total, plus, minus, mul, div) : 
    global max_ans, min_ans
    
    if idx == n :
        max_ans = max(max_ans, total)
        min_ans = min(min_ans, total)
        return

    if plus > 0 :
        dfs(idx+1, total+arr[idx], plus-1, minus, mul, div)
        
    if minus > 0 :
        dfs(idx+1, total-arr[idx], plus, minus-1, mul, div)
    
    if mul > 0 :
        dfs(idx+1, total*arr[idx], plus, minus, mul-1, div)

    if div > 0 :
        if total < 0 :
            dfs(idx+1, -(-total//arr[idx]), plus, minus, mul, div-1)
        else :
            dfs(idx+1, total//arr[idx], plus, minus, mul, div-1)
    

plus, minus, mul, div = four[0], four[1], four[2], four[3]
dfs(1, arr[0], plus, minus, mul, div)
print(max_ans)
print(min_ans)