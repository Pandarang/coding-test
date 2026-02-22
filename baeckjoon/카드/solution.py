n = int(input())
arr = [int(input()) for _ in range(n)]

dic = {}
for d in arr :
    dic[d] = dic.get(d, 0) + 1
    
max_d = max(dic.items(), key=lambda x: x[1])
min_d = 2**62 + 1

for k, v in dic.items() :
    if v == max_d[1] :
        min_d = min(min_d, k)
        
print(min_d)