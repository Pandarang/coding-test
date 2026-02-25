key = input().strip()
st = input().strip()

k = len(key)
n = len(st)
rows = n // k

order = sorted(range(k), key=lambda x: (key[x], x))

table = [[''] * k for _ in range(rows)]
p = 0
for col in order :
    for r in range(rows) :
        table[r][col] = st[p]
        p += 1

print(''.join(''.join(row) for row in table))