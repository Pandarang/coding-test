

def area(x1, y1, x2, y2) :
    return (x2 - x1) * (y2 - y1)

def distinct(a, b) :
    x1 = min(a[3], b[3]) 
    x2 = max(a[1], b[1])
    y1 = min(a[2], b[2])
    y2 = max(a[0], b[0])

    if x2 - x1 > 0 and y2 - y1 > 0 :
        return 0
    else :
        return abs((x2 - x1) * (y2 - y1))

arr = [list(map(int, input().split())) for _ in range(4)]

answer = 0
for a, b, c, d in arr :
    answer += area(a, b, c, d)
    print(answer)

for i in range(4) :
    for j in range(i+1,4) :
        answer -= distinct(arr[i], arr[j])

print(answer)
    