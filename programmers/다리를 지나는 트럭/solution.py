from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    times = 0
    cur_weight = 0
    
    while trucks or cur_weight > 0 :
        times += 1
        
        cur_weight -= bridge.popleft()
        
        if trucks and cur_weight + trucks[0] <= weight :
            t = trucks.popleft()
            bridge.append(t)
            cur_weight += t
        else :
            bridge.append(0)
            
    return times