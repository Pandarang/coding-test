T = int(input())
for _ in range(T) :
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    board = []

    dp = [[0] * m for _ in range(n)]
    dp[0][0] = board[0]
    
    for i in range(1, n) :
        for j in range(1, m) :
            dp[i][j] += max(board[i-1][j], board[i][j-1], board[i-1][j-1])

    print(dp)
    