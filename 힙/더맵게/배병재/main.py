import heapq
def solution(scoville, K):
    ans=0
    heapq.heapify(scoville)
    while True:
        if len(scoville)==1:
            return -1
        a=heapq.heappop(scoville)
        b=heapq.heappop(scoville)
        heapq.heappush(scoville,(a+b*2))
        ans+=1
        c=heapq.heappop(scoville)
        if c>=K:
            break
        else:
            heapq.heappush(scoville,c)
    print(ans)
    return ans


solution([1,1,1,1,3],3)