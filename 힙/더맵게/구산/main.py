import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        first_min = heapq.heappop(scoville)
        second_min = heapq.heappop(scoville)
        heapq.heappush(scoville,first_min + second_min * 2)
        answer += 1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    return answer


scoville = [1,2,3,9,10,12]
K = 7
print(solution(scoville, K))