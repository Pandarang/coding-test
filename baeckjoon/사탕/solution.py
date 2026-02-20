import sys
input = sys.stdin.readline

n = int(input())
b = [int(input()) for _ in range(n)]  

alt = 0
for i in range(n):
    if i % 2 == 0:   
        alt += b[i]
    else:            
        alt -= b[i]
a1 = alt // 2

a = [0] * n
a[0] = a1

for i in range(n - 1) :
    a[i + 1] = b[i] - a[i]

for x in a :
    print(x)