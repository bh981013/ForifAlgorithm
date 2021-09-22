def solution(participant, completion):
    for c in completion:
        participant.remove(c)
    answer = participant[0]
    return answer

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))
