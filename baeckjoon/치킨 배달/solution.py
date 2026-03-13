from itertools import combinations
INF = int(1e9)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chickens = []
houses = []
answer = INF

for y in range(n) :
    for x in range(n) :
        if arr[y][x] == 2 :
            chickens.append((y, x))
        elif arr[y][x] == 1 :
            houses.append((y, x))

for comb in combinations(chickens, m) :
    total = 0
    for hx, hy in houses :
        dist = INF
        for cx, cy in comb :
            dist = min(dist, abs(cx - hx) + abs(cy - hy))
        total += dist
    answer = min(answer, total)
    
print(answer)
