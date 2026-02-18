b, c, d = map(int, input().split())
arr = [b, c, d]
m_arr = min(b, c, d)
b = b - m_arr
c = c - m_arr
d = d - m_arr

burger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))
burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)

total = sum(burger) + sum(side) + sum(drink)
print(total)

sale_total = 0
for i in range(m_arr) :
    sale_total += burger[i]
    sale_total += drink[i]
    sale_total += side[i]
sale_total = sale_total * 0.9

if b > 0 :
    for i in burger[-b:] :
        sale_total += i
if c > 0 :
    for i in side[-c:]:
        sale_total += i
if d > 0 :
    for i in drink[-d:] :
        sale_total += i
print(int(sale_total))
