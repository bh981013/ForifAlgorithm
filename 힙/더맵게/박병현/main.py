import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(scoville):
        popped = heapq.heappop(scoville)
        if popped >= K:
            return answer
        else:
            if scoville:
                popped2 = heapq.heappop(scoville)
            else:
                return -1
            heapq.heappush(scoville, popped+ 2*popped2)
            answer+=1
    return answer