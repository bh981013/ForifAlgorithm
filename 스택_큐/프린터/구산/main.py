def solution(priorities, location):
    list_print = []
    answer = []
    for i in range(len(priorities)):
        list_print.append((i, priorities[i]))
    while True:
        if len(list_print) <= 1:
            answer.append(list_print[0][0])
            break
        for i in range(1,len(list_print)):
            if list_print[0][1] < list_print[i][1]:
                last_print = list_print.pop(0)
                list_print.append(last_print)
                break
            elif i == len(list_print) - 1:
                answer.append(list_print.pop(0)[0])
                break

    return answer.index(location)+1


priorities = [1,1,9,1,1,1]
location = 0
print(solution(priorities, location))