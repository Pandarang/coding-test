n = int(input())

ans = n * 100
arr = []

for _ in range(n) :
    arr.append(list(map(int, input().split())))
    
ft = [[False] * 100 for _ in range(100)]

for w, h in arr :
    for i in range(w, w+10) :
        for j in range(h, h+10) :
            ft[i][j] = True

cnt = 0
for i in range(100) :
    for j in range(100) :
        if ft[i][j] == True :
            cnt += 1
print(cnt)