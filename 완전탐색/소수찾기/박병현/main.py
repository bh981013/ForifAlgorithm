import itertools
def isprime(num):
    if num == 0 or num == 1: return 0
    for i in range(2, int((num**1/2))+1):
        if num % i == 0:
            return 0
    return 1
A = []
def getnum(numbers, gotnum, left, index):
    if left == 0:
        arr = list(map("".join, list(itertools.permutations(gotnum)))) 
        for a in arr:
            A.append(int(a))
        return
    for i in range(index, len(numbers)):
        getnum(numbers, gotnum + numbers[i], left-1, i+1)

def solution(numbers):
    global A
    answer= 0
    for i in range(1, len(numbers)+1):
        getnum(numbers, "", i, 0)
    B = set(A)
    for b in B:
        answer += isprime(b)
    return answer
