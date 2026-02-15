def solution(routes):
    routes.sort(key=lambda x: x[1])
    print(routes)
    
    cameras = 0
    cam_pos = -30001
    
    for start, end in routes :
        if cam_pos < start :
            cameras += 1
            cam_pos = end
            
    return cameras
    
