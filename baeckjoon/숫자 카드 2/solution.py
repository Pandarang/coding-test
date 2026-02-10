import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
answer = [0] * len(find)

dic = {}

for d in cards :
    dic[d] = dic.get(d, 0) + 1


for i in range(len(find)) :
    answer[i] = dic.get(find[i], 0)
    
print(*answer)