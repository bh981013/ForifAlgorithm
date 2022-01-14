from operator import le
import sys
import copy
from collections import deque
import heapq
import math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
printf = sys.stdout.write

arr = [i for i in range(14)] + [i for i in range(12, 0, -1)]
done = []
length = 0
cur = 0

A = ord('A')

def solution(name):
    global length
    ret = 0
    length = len(name)
    for n in name:
        ret += arr[ord(n) - A]  #상하 이동 횟수 미리 더함
    
    # 1) A가 나타나는 구간을 전부 구함
    scope = []  #구간 리스트들을 저장
    i = 1
    while(i<length):
        start, end = 0,0
        if name[i] == 'A':
            start = i
            for j in range(start, length):
                if name[j] != 'A':
                    break
                end = j
            scope.append([start, end])
            i = end+1
        else:
            i += 1
    #각 구간별로 왼쪽과 오른쪽에 해당하는 부분으로 나눔
    #2x왼쪽+오른쪽 or 2x오른쪽+왼쪽 중 더 작은값으로 선택
    #모든 구간중 가장 작은 결과값을 가진것이 정답
    minimum = length-1
    for start, end in scope:
        leftLength = start - 1
        rigthLength = length - end - 1
        minimum = min(minimum, 2*leftLength+rigthLength, 2*rigthLength+leftLength)
    
    return ret + minimum

#기존에는 각 경우마다 변경해야하는 칸중 가장 가까운곳으로 이동하는것으로 생각했지만, 틀림.