n = int(input())
arr = [int(input()) for _ in range(n)]

for x in arr :
    fib = [1, 2]
    while fib[-1] <= x :
        fib.append(fib[-1] + fib[-2])

    ans = []
    for f in reversed(fib) :
        
        if f <= x :
            ans.append(f)
            x -= f
        if x == 0 :
            break
    
    ans.sort()
    print(*ans)