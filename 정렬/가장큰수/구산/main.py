def solution(numbers):
    answer = ''
    temp = list(map(str, numbers))
    for i in range(len(temp)):
        if len(temp[i]) == 1:
            n = temp[i]
            temp[i] += (n + n + n)
        elif len(temp[i]) == 2:
            n = temp[i][-1]
            temp[i] += (n + n)
        elif len(temp[i]) == 3:
            temp[i] += temp[i][-1]
    temp = list(map(int, temp))
    list_temp = list(zip(numbers, temp))
    list_temp = sorted(list_temp, key=lambda x: (x[1], -x[0]), reverse=True)
    for n in list_temp:
        answer += str(n[0])
    return answer


numbers = [3,30,34,5,9]
print(solution(numbers))
