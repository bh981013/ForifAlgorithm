def solution(participant, completion):
    hash_participant = {}
    for p in participant:
        if p in hash_participant:
            hash_participant[p] += 1
        else:
            hash_participant[p] = 1
    for c in completion:
        if hash_participant[c] == 1:
            del hash_participant[c]
        else:
            hash_participant[c] -= 1
    return list(hash_participant.keys())[0]

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))
