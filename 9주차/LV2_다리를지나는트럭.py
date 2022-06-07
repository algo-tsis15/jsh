def solution(bridge_length, weight, truck_weights):
    sec=-1
    bridge=[0]*bridge_length
    while True:
        sec+=1
        if not truck_weights:
            if sum(bridge)==0:
                return sec
            else:
                bridge.insert(0,0)
                del bridge[-1]
                continue
        del bridge[-1]
        if sum(bridge)+truck_weights[0]<=weight:
            bridge.insert(0,truck_weights.pop(0))
        else:
            bridge.insert(0,0)