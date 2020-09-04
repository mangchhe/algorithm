""" 
    작성일 : 20/09/03 - 진행중
    수정일 : 20/09/04 - 완료
"""

def solution(bridge_length, weight, truck_weights):

    bridge_truck = []
    length_count = []
    tm = 0

    while True:

        if truck_weights and  sum(bridge_truck) + truck_weights[0] <= weight:
            bridge_truck.append(truck_weights[0])
            del truck_weights[0]
            length_count.append(0)

        length_count = list(map(lambda x: x+1, length_count))

        if length_count[0] == bridge_length:
            del bridge_truck[0]
            del length_count[0]
        
        if not truck_weights + length_count:
            break

        tm += 1
    
    return tm + 2

print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))