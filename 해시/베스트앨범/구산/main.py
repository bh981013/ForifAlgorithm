def solution(genres, plays):
    genre_play = list(zip(genres, plays))
    dict_genre = {}
    answer = []

    for gp in genre_play:
        if gp[0] in dict_genre.keys():
            dict_genre[gp[0]] += gp[1]
        else:
            dict_genre[gp[0]] = gp[1]
    genre_priority = sorted(dict_genre.items(), key= lambda x: x[1], reverse=True)
    for genre in genre_priority:
        dict = {}
        for i in range(len(genre_play)):
            if genre_play[i][0] == genre[0]:
                dict[i] = genre_play[i][1]
        list_index = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        answer.append(list_index[0][0])
        if len(list_index) >= 2:
            answer.append(list_index[1][0])

    genre_play = sorted(genre_play, key=lambda x: x[0])
    return answer


genres = ["classic", "pop", "classic", "classic", "pop", "pop"]
plays = [500, 2500, 150, 800, 2500, 3000]

print(solution(genres, plays))
