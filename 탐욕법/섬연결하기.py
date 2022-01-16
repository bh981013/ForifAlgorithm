'''
1.(초기)비용 가장 작은 길 선택
2.(반복)그 길에 연결된 두 섬과 연결된 길중에, 다른 섬과 아직 연결이 안된 가장 비용 작은 길 선택
3.추가된 섬을 포함한 연결된 길중,가장 비용작은 길 선택
4.모든 섬이 포함되면 종료
'''

import heapq
from tkinter.tix import Tree
def solution(n, costs):
    answer = 0
    remain = n #연결해야하는 남은 섬 개수
    heap = []
    done = [False for _ in range(n)]
    E = [[]for _ in range(n)]   #index번째와 연결된 섬, 그 가격->E[u] = [v, w]
    minE = costs[0]
    minW = costs[0][2]
    for u, v, w in costs:
        E[u].append([v,w])
        E[v].append([u,w])
        if minW > w:
            minE = [u,v,w]
            minW = w
    initV1 = minE[0]
    initV2 = minE[1]
    # print("초기V:", initV1, initV2)
    done[initV1] = True
    done[initV2] = True
    answer += minW
    for adjV, adjW in E[initV1]:
        if adjV != initV2:
            heapq.heappush(heap, [adjW, initV1, adjV])
    for adjV, adjW in E[initV2]:
        if adjV != initV1:
            heapq.heappush(heap, [adjW, initV2, adjV])
    remain -= 2
    while(remain):
        oldV, newV = 0,0
        w, v, u = heapq.heappop(heap)
        if(done[v] and done[u]): continue
        remain -= 1
        if done[v] and not done[u]:
            oldV = v
            newV = u
        else:
            oldV = u
            newV = v
        # print("기존V", oldV, "새로운 V:", newV)
        done[newV] = True
        answer += w
        for adjV, adjW in E[newV]:
            if(not done[adjV]):
                # print("heap에 V:", adjV, "w:", adjW, "추가")
                heapq.heappush(heap,[adjW, newV, adjV])
                
    return answer
print(solution(4,[[0,1,1],[0,2,1],[1,2,1],[1,3,2],[2,3,2]]))

'''
최종: 매우 빨리 해결하였다. 각 경우에 선택할 수 있는 최선은 연결된 edge중 아무것도 연결이 안된 가장 싼 edge라는 점을 이용하였다.
전체와 연결되는 섬에서 특정 섬으로 가기 위해선 가장 가격이 낮은 길을 선택해야 한다는 점을 귀납적으로 생각하였다.
만약 어떤 섬으로 가기 위에서 고른 길보다 더 가격이 높은최적해가 존재한다면, 언제나 더 가격이 낮은 길로 대체하는 최적해가 언제나 존재하기 때문이다.
'''