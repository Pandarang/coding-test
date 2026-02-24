n = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
dic = {}
x, y = 0, 0
xx, yy = 0, 0

for a, b in arr :
    dic.setdefault(a, []).append(b)
    
if len(dic[1]) > len(dic[2]) :
    x = max(dic[2], dic[4])
    y = min(dic[2], dic[4])
    for i, (a, b) in enumerate(arr) :
        if a == 1 :
            xx = dic[1][1]
            yy = dic[3][0]
            break
        elif a == 3 :
            xx = dic[1][0]
            yy = dic[3][1]
            break
else :
    x = max(dic[1], dic[3])
    y = min(dic[1], dic[3])
    xx = dic[2][0]
    yy = dic[4][1]
    for i, (a, b) in enumerate(arr) :
        if a == 2 :
            xx = dic[2][1]
            yy = dic[4][0]
            break
        elif a == 4 :
            xx = dic[2][0]
            yy = dic[4][1]
            break


area = x[0] * y[0] - xx * yy
print(area * n)