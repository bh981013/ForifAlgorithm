#k개의 수를 뺄 수 있을때, 앞에서 k+1개중 가장 큰수를 찾아서 그 앞에있는 모든수를 뺌
#위 작업을 k=0 이 될때까지 반복
import heapq

def solution(number, k):
    answer = []
    numberList = list(map(int, list(number)))
    length = len(number)
    index = -1
    maxIndex = -1
    heap = []
    delRemain = k
    jump = 0
    #처음 k+1개를 확인
    #k+1개를 전부 확인했다면, 가장 큰 값을 answer에 추가하고 maxIndex를 통해 삭제해야 하는 숫자 개수(k_) 감소
    #(반복)그 다음 숫자를 heap에 추가->[-number, index]형식
    #pop했는데 index가 maxIndex보다 작다면, 다시 pop함
    #pop했는데 index가 maxIndex보다 크다면, maxIndex 를 index값으로 설정하고, k값 결정, number을 answer에 추가
    #k가 0이 되면 더이상 삭제할수 없으므로, 반복 종료
    for i in range(k+1):
        heapq.heappush(heap, [-numberList[i], i])
    while(True):
        popped = heapq.heappop(heap)
        poppedNum = -popped[0]
        poppedIndex = popped[1]
       # print("poppedNum: ", poppedNum)
        if poppedIndex <maxIndex:
           # print("뒤에꺼임")
            continue
        else:
            #print("삭제가능")
            delRemain = delRemain -(poppedIndex - maxIndex - 1)   #새로운 답과 기존 답 사이의 값들은 삭제한것임
            #print("남은 삭제개수:", delRemain)
            maxIndex = poppedIndex
            #print(poppedNum)
            answer.append(poppedNum)
            if(delRemain == length - maxIndex-1): return "".join(map(str,answer))
            if(delRemain != 0):
                heapq.heappush(heap,[-numberList[k+1 + jump], k+1+jump])
                jump += 1
                #print("heap에", numberList[maxIndex+1], "추가")
            else:
                break
    for n in numberList[maxIndex+1:]:
        answer.append(n)
    answer = "".join(map(str,answer))
    return answer


#최종: 이게 생각보다 어려웠다.. 그리디라서 heapq를 쓸 필요가 없다고 생각했지만, 쓰고 잘 풀렸다.
#하지만 stack을 사용해서 더욱 빠르게 풀 수 있는 방법이 있었다.
#하지만 그 방법이 조금 납득하기 힘들다......

