from collections import Counter

n = int(input())

arr = []
words = [input().strip() for _ in range(n)]

def p(x) :
    dic = {}
    res = []
    idx = 0
    for ch in x :
        if ch not in dic :
            dic[ch] = idx
            idx += 1
        res.append(str(dic[ch]))
    return ''.join(res)

cnt = 0
for i in range(n) :
    pi = p(words[i])
    for j in range(i + 1, n) :
        if pi == p(words[j]) :
            cnt += 1

print(cnt)