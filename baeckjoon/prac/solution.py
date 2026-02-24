from itertools import permutations

n, m = input().split()

new_n = list(n)

temp = set()

for p in permutations(new_n, len(n)) :
    if p[0] == '0' :
        continue
    temp.add(int(''.join(p)))

m = int(m)
answer = 0
for i in temp :
    if i > m :
        continue
    if i > answer :
        answer = i

if answer == 0 :
    print(-1)
else :
    print(answer)