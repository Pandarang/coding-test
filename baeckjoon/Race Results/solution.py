n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[0], x[1], x[2]))

for i in arr :
    print(*i)