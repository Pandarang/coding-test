a = int(input())

for _ in range(a) :
    n = int(input())

    fib = [1, 2]
    while fib[-1] <= n :
        fib.append(fib[-1] + fib[-2])

    remain = n
    ans = []

    for f in reversed(fib) :
        if f <= remain :
            ans.append(f)
            remain -= f
        if remain == 0 :
            break

    print(*sorted(ans))

