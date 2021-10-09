from collections import deque

def solution(progresses, speeds):
    answer = []
    arr = []
    i  = 0
    N = len(progresses)
    for p, s in zip(progresses, speeds):
        temp = (100- p) // s
        if (100-p)%s>0:
            p = temp+1
        else:
            p = temp
        arr.append([p,i])
        i += 1
    arr.sort(key= lambda x: x[0])
    arr = deque(arr)
    next = 0
    done = [0 for _ in range(N)]
    day = 0
    while arr:
        found = False
        while arr and arr[0][0] == day:
            prior, seq = arr.popleft()
            done[seq] = 1
            if seq == next:
                found = True
        if found:
            donenum = 0
            while(next<N and done[next]):
                next+=1
                donenum+=1
            answer.append(donenum)
        day+=1

    return answer
