import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * m for _ in range(n)]
res = []

for y in range(n):
    for x in range(m):
        if arr[y][x] != '*':
            continue

        lens = []
        for i in range(4):
            length = 0
            ny = y + dy[i]
            nx = x + dx[i]
            while 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == '*':
                length += 1
                ny += dy[i]
                nx += dx[i]
            lens.append(length)

        k = min(lens)
        if k >= 1:

            res.append((y + 1, x + 1, k))

            visited[y][x] = True
            for i in range(4):
                ny, nx = y, x
                for _ in range(k):
                    ny += dy[i]
                    nx += dx[i]
                    visited[ny][nx] = True

ok = True
for y in range(n):
    for x in range(m):
        if arr[y][x] == '*' and not visited[y][x]:
            ok = False
            break
    if not ok:
        break

if not ok:
    print(-1)
else:
    print(len(res))
    for y, x, k in res:
        print(y, x, k)