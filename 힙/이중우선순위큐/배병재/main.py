import heapq
def solution(operations):
    min_heap=[]
    max_heap=[]
    d=0
    i=0
    for op in operations:
        result=op.split()
        value=int(result[1])
        if result[0]=='I':
            i+=1
            heapq.heappush(min_heap,value)
            heapq.heappush(max_heap,(-value,value))
        else:
            d+=1
            if i<d:
                d-=1
                continue
            if value<0:
                heapq.heappop(min_heap)
            else:
                heapq.heappop(max_heap)
        if i==d:
            min_heap=[]
            max_heap=[]
    if i==d:
        return [0,0]
    else:
        return [heapq.heappop(max_heap)[1],heapq.heappop(min_heap)]