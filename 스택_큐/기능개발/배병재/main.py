import math
def solution(progresses, speeds):
    answer=[]
    days=[]
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    ans=0
    day=days[0]
    for idx,i in enumerate(days):
            print(day)
            if day>=i:
                ans+=1
            else:
                answer.append(ans)
                ans = 1
                day=i
            if idx == len(days) - 1:
                answer.append(ans)
    return answer
