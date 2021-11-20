def yaksu(num):
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
    return result

def solution(brown, yellow):
    answer = []
    list_yaksu = yaksu(yellow)
    for i in range(int(len(list_yaksu)/2)+1):
        tuple_yaksu = (list_yaksu[len(list_yaksu)-i-1],list_yaksu[i])
        if tuple_yaksu[0] * 2 + tuple_yaksu[1] * 2 + 4 == brown:
            answer = [tuple_yaksu[0] + 2, tuple_yaksu[1] + 2]
            break
    return answer

brown = 24
yellow = 24
print(solution(brown, yellow))