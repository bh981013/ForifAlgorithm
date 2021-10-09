def solution(participant, completion):
    people = {}
    answer = ""
    for c in completion:
        if not people.get(c):
            people[c] = 1
        else:
            people[c] += 1
    for p in participant:
        if people.get(p):     
            people[p] -= 1
        else:
            answer = p
            break
    return answer