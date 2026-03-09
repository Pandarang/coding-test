from itertools import combinations

n, m = map(int, input().split())

arr = list(input().split())
arr.sort()
alp = {'a', 'e', 'i', 'o', 'u'}

ans = []

for word in combinations(arr, n) :
    a = 0
    b = 0
    
    for ch in word :
        if ch in alp :
            a += 1
        else :
            b += 1
    
    if a >= 1 and b >= 2 :
        print(''.join(word))