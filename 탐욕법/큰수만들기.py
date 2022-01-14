#k개의 수를 뺄 수 있을때, 앞에서 k+1개중 가장 큰수를 찾아서 그 앞에있는 모든수를 뺌
#위 작업을 k=0 이 될때까지 반복


def solution(number, k):
    answer = []
    #numberList = list(map(int, list(number)))
    index = 0
    maxIndex = 0
    while(k>0):
        maxNum = -1
        if(index + k == len(number)):    #만약 남은 숫자개수랑 k개수랑 같다면, 즉시 종료
            return "".join(map(str,answer))
        
        for i in range(index, index + k+1):    #가장 큰 수를 찾음
            if maxNum < int(number[i]):
                maxNum = int(number[i])
                maxIndex = i
        answer.append(maxNum)
        k = k - (maxIndex - index)
        index = maxIndex + 1
    for n in (number[maxIndex+1:]):
        answer.append(int(n))
    answer = "".join(map(str,answer))
    return answer
string = "1924"
print(solution(string , 2))