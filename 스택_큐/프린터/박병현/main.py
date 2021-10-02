from collections import deque

def solution(priorities, location):
    answer = 0
    target = 10
    arr = deque()
    for i in range(len(priorities)):
        arr.append([priorities[i],i])
    prnum = [0 for _ in range(11)]
    for p in priorities:
        prnum[p] += 1
    for i in range(10,0,-1):
        if prnum[i] != 0:
            target = i
            break
    while(arr):
        popped, index = arr.popleft()
        if popped != target:
            arr.append([popped, index])
        else:
            prnum[popped] -= 1
            answer += 1
            if index == location:
                break
            if prnum[popped] == 0:
                for i in range(popped-1,0,-1):
                    if prnum[i] != 0:
                        target = i
                        break
    return answer
