n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()

xs = [i[0] for i in arr]
hs = [i[1] for i in arr]

max_h = max(hs)
max_idx = hs.index(max_h)

area = 0

cur_h = hs[0]
cur_x = xs[0]

for i in range(1, max_idx + 1) :
    if hs[i] >= cur_h :
        area += cur_h * (xs[i] - cur_x)
        cur_h = hs[i]
        cur_x = xs[i]

cur_h = hs[-1]
cur_x = xs[-1]

for i in range(n - 2, max_idx - 1, -1) :
    if hs[i] >= cur_h:         
        area += cur_h * (cur_x - xs[i])
        cur_h = hs[i]
        cur_x = xs[i]
    
area += max_h
print(area)