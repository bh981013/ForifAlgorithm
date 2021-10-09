def solution(prices):
    answer = []
    for i in range(len(prices)):
        for j in range(i,len(prices)):
            if prices[j] < prices[i]:
                answer.append(j-i)
                break
            elif j == len(prices) - 1:
                answer.append(j-i)
    return answer


prices = [1,2,3,2,3]
print(solution(prices))