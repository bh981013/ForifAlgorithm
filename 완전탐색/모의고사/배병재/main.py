def solution(answers):
    answer = []  
    scores = [0,0,0]
    ans1 = [1,2,3,4,5]
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for ind in range(len(answers)):
        if ans1[ind%5]==answers[ind] :
            scores[0] += 1

        if ans2[ind%8]==answers[ind] :
            scores[1] += 1

        if ans3[ind%10]==answers[ind] :
            scores[2] += 1

    maxScore = max(scores)

    for i in range (len(scores)): 
        if scores[i] == maxScore:
            answer.append(i+1)
    return answer