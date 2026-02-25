import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
oil = list(map(int, input().split()))

ans = 0

for i in range(n-1) :
    if oil[i] >= oil[i+1] :
        ans += oil[i] * distance[i]
    else :
        ans += oil[i] * distance[i]
        oil[i+1] = oil[i]

print(ans)
