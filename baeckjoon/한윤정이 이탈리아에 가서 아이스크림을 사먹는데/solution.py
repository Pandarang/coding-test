from itertools import combinations

n, m = map(int, input().split())

bad = set()

for _ in range(m) :
    a, b = map(int, input().split())
    if a > b :
        a, b = b, a
    bad.add((a, b))

ans = 0
for a, b, c in combinations(range(1, n + 1), 3) :
    if (a, b) in bad or (a, c) in bad or (b, c) in bad :
        continue
    ans += 1

print(ans)
