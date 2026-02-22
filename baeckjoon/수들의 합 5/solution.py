n = int(input())

end = 1
start = 1
count = 1
cur_val = 1

while end != n :
    if cur_val == n :
        count += 1
        end += 1
        cur_val += end
        
    elif cur_val < n :
        end += 1
        cur_val += end
        
    else :
        cur_val -= start
        start += 1
        
print(count)