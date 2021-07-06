from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    q = deque(truck_weights)
    now_weight = 0

    while q:
        time += 1
        out = bridge.popleft()
        now_weight -= out

        if now_weight + q[0] <= weight:
            truck_weight = q.popleft()
            bridge.append(truck_weight)
            now_weight += truck_weight
        else:
            bridge.append(0)
    for i in range(bridge_length - 1, -1, -1):
        if bridge[i] != 0:
            time += (i + 1)
            break
    return time

solution(2, 10, [7,4,5,6])