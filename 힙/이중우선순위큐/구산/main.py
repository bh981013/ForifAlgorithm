import heapq


def solution(operations):
    answer = []
    heapq.heapify(answer)
    for o in operations:
        command, num = o.split(" ")
        num = int(num)
        if command == "I":
            heapq.heappush(answer, num)
        elif command == "D" and answer != []:
            if num == -1:
                heapq.heappop(answer)
            elif num == 1:
                answer.pop(-1)

    if len(answer) == 0:
        return [0, 0]

    return [max(answer), answer[0]]


operations = ["I 5", "I 5", "I 5"]
print(solution(operations))
