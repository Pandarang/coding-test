a = input()
cnt = 0
l = []
li = []

for i in a :
    li.append(i)

for x in li :
    if x == '(' :
        l.append(x)
        cnt += 1
    elif x == ')' and len(l) == 0 :
        cnt += 1
    else :
        l.pop()
        cnt -= 1
print(cnt)
