def solution(clothes):
    answer=1
    li=[]
    dict={}
    for clothe in clothes:
        if clothe[1] not in li:
            li.append(clothe[1])
        if dict.get(clothe[1]):
            dict[clothe[1]]+=1
        else:
            dict[clothe[1]]=1
    for l in li:
        answer*=(dict[l]+1)
    answer-=1
    return answer
