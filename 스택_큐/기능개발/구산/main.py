def solution(progresses, speeds):
    answer = []
    while True:
        if not progresses:
            break
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        count = 0
        while True:
            if len(progresses) > 0 and progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            else:
                break
        if count > 0:
            answer.append(count)
    return answer


progresses = [10,20,30,40]
speeds = [40,30,20,10]

print(solution(progresses, speeds))
