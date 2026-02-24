s = input().strip()
n = int(input())
arr = [input() for _ in range(n)]

def repl(s, k) :
    res = ""
    for c in s :
        x = ord(c) + 97

        res += chr((x + k) % 26 + 97)

    return res

for k in range(26) :
    card = repl(s, k) 
    for w in arr :
        if w in card :
            print(card)
            exit()


