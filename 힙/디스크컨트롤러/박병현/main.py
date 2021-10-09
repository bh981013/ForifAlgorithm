import heapq
from collections import deque
def solution(jobs):
    answer = 0
    jobs.sort()
    arr = deque(jobs)
    print(arr)
    time = 0
    q= []
    while(arr or q):
        if not q:
            time = arr[0][0]
        else:
            length, start = heapq.heappop(q)
            time += length
            answer+= time-start
        while(arr):
            if arr[0][0] <= time:
                popped = arr.popleft()
                heapq.heappush(q, [popped[1], popped[0]])
            else:
                break
    return int(answer/len(jobs))

