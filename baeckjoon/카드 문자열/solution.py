from collections import deque

n = int(input())


for _ in range(n) :
    d = deque()
    m = int(input())
    s = input().split(" ")

    for ch in s :
        if len(d) == 0 :
            d.append(ch)
        elif ch > d[0] :
            d.append(ch)
        else :
            d.appendleft(ch)
    print(''.join(d))


