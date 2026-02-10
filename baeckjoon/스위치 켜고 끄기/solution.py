n = int(input())

switch = list(map(int, input().split()))

stu = int(input())

arr = [list(map(int, input().split())) for _ in range(stu)]

for (a, b) in arr :
    if a == 1 :
        for i in range(b-1, n, b) :
            switch[i] ^= 1
    else :
        left = b- 1
        right = b -1

        while left - 1 >= 0 and right + 1 < n and switch[left-1] == switch[right+1] :
            left -= 1
            right += 1

        for i in range(left, right + 1) :
            switch[i] ^= 1

for i in range(n) :
    print(switch[i], end= " ")
    if (i + 1) % 20 == 0 :
        print()
