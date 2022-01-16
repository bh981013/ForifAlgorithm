'''
가장 무거운 사람과 가장 가벼운 사람을 매칭.
만약 limit보다 크다면, 무거운사람만 타게 함.
남은사람이 없을때까지 반복함
'''

from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while(people):
        if(len(people) == 1):
            answer += 1
            break
        lightest = people[0]
        heaviest = people[-1]
        if(lightest + heaviest <= limit):
            answer += 1
            people.popleft()
            people.pop()
        else:
            answer+=1
            people.pop()
    return answer
'''
10 10 20 20 / 30 -> 어떻게 가지??
정답: 2번인데.....
웬만해선 딱 맞춰서 태우기??
--------------------------------------------
최종:
사실 엄청 쉬운 문제였다. 문제를 꼼꼼히 읽지 않아 오랫동안 고민하였다.
구명보트에 2명밖에 못탄다는 점을 확인했어야 한다....

'''

