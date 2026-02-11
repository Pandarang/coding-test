n = int(input())

switch = list(map(int, input().split()))
stu = int(input())

for _ in range(stu) :
    a, b = map(int, input().split())

    if a == 1 :
        for i in range(b-1, n, b) :
            switch[i] ^= 1
            
    else :
        left, right = b - 1, b - 1
        
        while left - 1 >= 0 and right + 1 < n and switch[left-1] == switch[right+1] :
            left -= 1
            right += 1
            
        for i in range(left, right+1, 1) :
            switch[i] ^= 1
    
for i in range(n):
    print(switch[i], end=" ")
    if (i + 1) % 20 == 0:
        print()