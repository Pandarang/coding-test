def solution(m, musicinfos):
    answer = ""
    
    m_arr = [s.split(",") for s in musicinfos]
    def conv(x):
        return (x.replace("C#", "c")
                 .replace("D#", "d")
                 .replace("F#", "f")
                 .replace("G#", "g")
                 .replace("A#", "a"))
    
    best = -1
    m = conv(m)
    
    for info in musicinfos:
        start, end, title, song = info.split(",")
        song = conv(song)

        sh, sm = map(int, start.split(":"))
        eh, em = map(int, end.split(":"))
        play = (eh - sh) * 60 + (em - sm)

        n = len(song)
        if play <= n :
            played = song[:play]
        else :
            played = song * (play // n) + song[:play % n]
        
        if m in played :
            if play > best :
                best = play
                answer = title
    
    return answer if answer else "(None)"
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        