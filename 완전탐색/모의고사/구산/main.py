def solution(answers):
    answer = [0, 0, 0]
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == s1[i % 5]:
            answer[0] += 1
        if answers[i] == s2[i % 8]:
            answer[1] += 1
        if answers[i] == s3[i % 10]:
            answer[2] += 1

    max_value = max(answer)
    result = []
    for i in range(len(answer)):
        if max_value == answer[i]:
            result.append(i+1)

    return result

answers = [1,3,2,4,2]
print(solution(answers))