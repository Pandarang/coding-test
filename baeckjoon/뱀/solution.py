from collections import deque

n = int(input())
k = int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
turn = [list(input().split()) for _ in range(l)]

board = [[0] * (n + 1) for _ in range(n + 1)]

for y, x in apple :
    board[y][x] = 1

snake = deque([(1, 1)])
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0
time = 0
idx = 0

while True :
    hy, hx = snake[-1]
    ny = hy + dirs[d][0]
    nx = hx + dirs[d][1]
    time += 1
    
    if ny < 1 or ny > n or nx < 1 or nx > n :
        break

    if (ny, nx) in snake:
        break

    snake.append((ny, nx))

    if board[ny][nx] == 1:
        board[ny][nx] = 0
    else:
        snake.popleft()
    
    if idx < l and time == int(turn[idx][0]) :
        if turn[idx][1] == 'D' :
            d = (d + 1) % 4
        else :
            d = (d - 1) % 4
        idx += 1

print(time)