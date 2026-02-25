s = input().strip()

def c_java(s) :    
    for i in s :
        if i.isupper() :
            return "Error!"
    a = s.split(" ")
    if len(a) > 1 :
        return "Error!"
    
    ans = s.split("_")
    res = ""
    for i in ans :
        res += i[0].upper() + i[1:]

    return res
def java_c(s) :
    ans = s.split(" ")
    res = ""
    if s[0].isupper() :
        return "Error!"
    if len(ans) > 1 :
        return "Error!"
    for i in s :
        if not i.isalpha() :
            return "Error!"
    
    for i in s :
        if i.isupper() :
            res += "_"
            res += i.lower()
        else :
            res += i
    return res


if java_c(s) != "Error!" :
    print(java_c(s))
elif c_java(s) != "Error!" :
    print(c_java(s))
elif java_c(s) == "Error!" and c_java(s) == "Error!" :
    print("Error!")
