import sys
input = sys.stdin.readline

p, m = map(int, input().split())
players = [list(input().split()) for _ in range(p)]



while len(players) >= m :
    stack = []
    stack.append((int(a), b))
    stand = 0
    for a, b in players :
        if len(stack) == m :
            print("Started")
            continue
        
        if abs(int(a) - stand) <= 10 :
            stack.append((int(a), b))


        
    stack.clear()
