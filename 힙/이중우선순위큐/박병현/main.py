import heapq
import copy
def solution(operations):
    answer = []
    minq = []
    maxq = []
    maxd = {}
    mind = {}
    for o in maxq:
        o[0] *= -1
    for o in operations:
        if o[0] == "I":
            heapq.heappush(minq,int(o[2:]))
            heapq.heappush(maxq,-int(o[2:]))
        elif o[0] == "D":
            if o[2] == "1":
                if maxq:
                    M = heapq.heappop(maxq)
                    while(maxd.get(M) and maxq):
                        maxd[M] -= 1
                        M = heapq.heappop(maxq)
                    if mind.get(-M):
                        mind[-M] += 1
                    else:
                        mind[-M] = 1
                        

            else:
                if minq:
                    M = heapq.heappop(minq)
                    while(mind.get(M) and minq):
                        mind[M] -= 1
                        M = heapq.heappop(minq)
                    if maxd.get(-M):
                        maxd[-M] += 1
                    else:
                        maxd[-M] = 1
    if not maxq or not minq:
        answer = [0,0]
    else:
        pop = heapq.heappop(maxq)
        while(maxd.get(pop) and maxq):
            pop = heapq.heappop(maxq)
        answer.append(-pop)

        pop = heapq.heappop(minq)
        while(mind.get(pop) and minq):
            pop = heapq.heappop(minq)
        answer.append(pop)
    return answer

