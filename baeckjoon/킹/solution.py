a, b, n = input().split(" ")

arr = [input() for _ in range(int(n)) ]

dic = {}
dic["R"] = [0, 1]
dic["L"] = [0, -1]
dic["B"] = [-1, 0]
dic["T"] = [1, 0]
dic["RT"] = [1, 1]
dic["LT"] = [1, -1]
dic["RB"] = [-1, 1]
dic["LB"] = [-1, -1]

def change(s) :
    li = [x for x in s]

    x = ord(li[0]) - 65 + 1
    y = int(s[1:])
    
    return (int(y), x)

def back(y, x) :
    s = chr(x + 65 - 1)
    y = str(y)
    
    return s + y
    
king_y, king_x = change(a)
rock_y, rock_x = change(b)


for c in arr :
    if c in dic :
        if 1 <= king_y + dic[c][0] <=8 and 1 <= king_x + dic[c][1] <= 8 :
                    if king_y + dic[c][0] == rock_y and king_x + dic[c][1] == rock_x :
                        if 1 <= rock_y + dic[c][0] <=8 and 1 <= rock_x + dic[c][1] <= 8 :
                            king_y, king_x = king_y + dic[c][0], king_x + dic[c][1]
                            rock_y, rock_x = rock_y + dic[c][0], rock_x + dic[c][1]
                        else :
                            continue
                    else :
                        king_y, king_x = king_y + dic[c][0], king_x + dic[c][1]
print(back(king_y, king_x))
print(back(rock_y, rock_x))
