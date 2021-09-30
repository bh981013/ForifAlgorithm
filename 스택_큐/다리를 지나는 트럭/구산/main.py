def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_weight = []
    while True:
        if not truck_weights and not bridge_weight:
            break

        answer += 1

        if bridge_weight and answer - bridge_weight[0][0] == bridge_length:
            bridge_weight.pop(0)

        if truck_weights and len(bridge_weight) <= bridge_length and sum(x[1] for x in bridge_weight) + truck_weights[
            0] <= weight:
            bridge_weight.append((answer, truck_weights.pop(0)))

    return answer


bridge_length = 100
weight = 100
truck_weights = [10]

print(solution(bridge_length, weight, truck_weights))
