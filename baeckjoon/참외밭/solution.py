n = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
dic = {}
x, y = 0, 0

for a, b in arr :
    dic.setdefault(a, []).append(b)

if len(dic[1]) > len(dic[2]) :
    x = max(dic[2], dic[4])
else :
    x = max(dic[1], dic[3])

    