n = int(input())

ans = 99
cnt = 0

if n <= 99 :
    ans = n
else :
    for num in range(100, n + 1) :
        num = str(num)
        if (int(num[0]) - int(num[1]) == int(num[1]) - int(num[2])) :
            ans += 1

print(ans)
