def solution(genres, plays):
    dict={}
    dict2={}
    answer=[]
    for i in range(len(genres)):
        genre=genres[i]
        play=plays[i]
        if dict.get(genre):
            dict[genre].append((i,play))
            dict2[genre]+=play
        else:
            dict[genre]=[(i,play)]
            dict2[genre]=play
    arr=list(dict2.items())
    arr.sort(key=lambda x:x[1],reverse=True)
    for i in arr:
        genre=i[0]
        dict[genre].sort(key=lambda x:x[1],reverse=True)
        for j in range(len(dict[genre])):
            if j<2:
                answer.append(dict[genre][j][0])
            else:
                break
    return answer
