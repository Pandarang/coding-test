n, m = map(int, input().split())
arr = [input().strip() for _ in range(n)]

a = n - 8 + 1
b = m - 8 + 1
answer = 65

def changeB(y, x) :
    cnt = 0
    for ny in range(y, 8+y) :
        for nx in range(x, 8+x) :
            if ny % 2 == 0 :
                if nx % 2 == 0 :
                    if arr[ny][nx] != 'B' :
                        cnt += 1
                else :
                    if arr[ny][nx] != 'W' :
                        cnt += 1
            else :
                if nx % 2 == 0 :
                    if arr[ny][nx] != 'W' :
                        cnt += 1
                else :
                    if arr[ny][nx] != 'B' :
                        cnt += 1
    return cnt

def changeW(y, x) :
    cnt = 0
    for ny in range(y, 8+y) :
        for nx in range(x, 8+x) :
            if ny % 2 == 0 :
                if nx % 2 == 0 :
                    if arr[ny][nx] != 'W' :
                        cnt += 1
                else :
                    if arr[ny][nx] != 'B' :
                        cnt += 1
            else :
                if nx % 2 == 0 :
                    if arr[ny][nx] != 'B' :
                        cnt += 1
                else :
                    if arr[ny][nx] != 'W' :
                        cnt += 1
    return cnt

for y in range(a) :
    for x in range(b) :
        answer = min(answer, changeB(y, x), changeW(y, x))


print(answer)
