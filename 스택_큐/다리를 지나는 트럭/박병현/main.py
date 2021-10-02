from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    arr = deque(truck_weights)
    intruck = deque([0 for _ in range(bridge_length)])
    curW = 0
    while(arr or (curW!= 0)):
        curW -= intruck.popleft()
        truck = 0
        if arr and curW+arr[0] <=weight:
            truck = arr.popleft()
        intruck.append(truck)
        curW += truck
        answer += 1
    return answer

print(solution(2,10,[7,4,5,6]))
