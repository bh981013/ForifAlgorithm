def solution(genres, plays):
    index = [i for i in range(len(genres))]
    answer = []

    d = {}
    for g, p, i in zip(genres, plays, index):
        if d.get(g):
            d[g].append([p,i])
        else:
            #qwe
            d[g] = [[p,i]]
    l = list(d.items())
    l.sort(key=getSum)
    for music in l:
        music[1].sort(key=lambda x:-x[0])
        answer.append(music[1][0][1])
        if len(music[1])>1:
            answer.append(music[1][1][1])
    return answer

def getSum(key_val):
    S = 0
    pairs = key_val[1]
    for p, i in pairs:
        S += p
    return -S