def solution(genres, plays):
    genre_play = list(zip(genres, plays))
    dict_genre = {}
    answer = []

    for gp in genre_play:
        if gp[0] in dict_genre.keys():
            dict_genre[gp[0]] += gp[1]
        else:
            dict_genre[gp[0]] = gp[1]
    genre_priority = sorted(dict_genre, key= lambda x: x[1], reverse=True)
    for genre in genre_priority:
        dict = {}
        for i in range(len(genre_play)):
            if genre_play[i][0] == genre:
                dict[genre_play[i][1]] = i
        list_index = sorted(dict.items(), key=lambda x: x[0], reverse=True)
        answer.append(list_index[0][1])
        if len(list_index) > 2:
            answer.append(list_index[1][1])

    genre_play = sorted(genre_play, key=lambda x: x[0])
    return answer


genres = ["classic"]
plays = [500]

print(solution(genres, plays))
