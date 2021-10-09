import heapq


def solution(jobs):
    answer = 0
    start = 0
    sorted_job = sorted(jobs, key=lambda x: x[1])

    while len(sorted_job) != 0:
        for i in range(len(sorted_job)):
            if sorted_job[i][0] <= start:
                start += sorted_job[i][1]
                answer += start - sorted_job[i][0]
                sorted_job.pop(i)
                break
            if i == len(sorted_job)-1:
                start += 1
    return answer // len(jobs)


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))
