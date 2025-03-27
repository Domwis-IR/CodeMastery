from collections import deque
def solution(bridge_length, weight, truck_weights):
    left_trucks = deque(truck_weights)
    first = left_trucks.popleft()
    on_bridge = deque([first])
    on_bridge_time = deque([1])
    time = 1
    
    while on_bridge:
        if time - on_bridge_time[0] == bridge_length - 1:
            on_bridge.popleft()
            on_bridge_time.popleft()
        time += 1
        if left_trucks:
            if sum(on_bridge) + left_trucks[0] <= weight and len(on_bridge) + 1 <= bridge_length:
                truck = left_trucks.popleft()
                on_bridge.append(truck)
                on_bridge_time.append(time)
    return time
    
    