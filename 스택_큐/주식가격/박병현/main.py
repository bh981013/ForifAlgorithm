from collections import deque
def solution(prices):
    N = len(prices)
    answer = [0 for _ in range(N)]
    index = 0
    for index in range(N):
        # if answer[index]:
        #     continue
        popped = prices[index]
        temp = [index]
        for i in range(index+1, N):
            if popped==prices[i]:
                temp.append(i)
            elif popped>prices[i]:
                break
        for t in temp:
            answer[t] = i-t
    answer[-1] = 0
    return answer
