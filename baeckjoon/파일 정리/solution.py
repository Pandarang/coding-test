import sys
input = sys.stdin.readline

arr = []
dic = {}

n = int(input())
for _ in range(n) :
    arr.append(input().strip().split(".")[1])

for x in arr :
    dic[x] = dic.get(x, 0) + 1

d = sorted(dic.items(), key=lambda x: x[0])

for k, v in d :
    print(k, v)

