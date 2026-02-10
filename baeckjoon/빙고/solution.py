import sys
input = sys.stdin.readline


board = [list(map(int, input().split())) for _ in range(5)]
answer = []
for _ in range(5) :
    answer += list(map(int, input().split()))
    
checked = [[False] * 5 for _ in range(5)]

pos = {}
for x in range(5) :
    for y in range(5) :
        pos[board[x][y]] = (x, y)

def bingo_count(bingo) :
    cnt = 0
    for i in range(5) :
        if all(bingo[i][j] for j in range(5)) :
            cnt += 1
    for j in range(5) :
        if all(bingo[i][j] for i in range(5)) :
            cnt += 1
    if all(bingo[i][i] for i in range(5)) :
        cnt += 1
    if all(bingo[i][4-i] for i in range(5)) :
        cnt += 1
    return cnt

for k, num in enumerate(answer, start=1) :
    x, y = pos[num]
    checked[x][y] = True
    
    if bingo_count(checked) >= 3 :
        print(k)
        break