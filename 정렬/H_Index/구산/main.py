def solution(citations):
    answer = 0
    citations = sorted(citations)
    for h in range(1,len(citations)+1):
        count = 0
        for i in range(len(citations)):
            if citations[i] >= h:
                count += 1

        if count >= h:
            answer = max(answer, h)
    return answer


citations = [3, 0, 6, 1, 5]
print(solution(citations))
