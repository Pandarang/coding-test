n = input().strip()

cnt = [0] * 10

for c in n :
    cnt[int(c)] += 1

cnt[6] = (cnt[6] + cnt[9] + 1) // 2
cnt[9] = 0

print(max(cnt))