n = int(input())
arr = list(map(int, input().split()))
s = set(arr)
dic = {}
ans = []

new_arr = sorted(s, key=lambda x: x)
for i, v in enumerate(new_arr) :
    dic[v] = i
    
for v in arr :
    if dic[v] is not None :
        ans.append(dic[v])
print(*ans)