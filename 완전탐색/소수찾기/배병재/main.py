import itertools
def solution(numbers):
    prime=[]
    answer=0
    number=list(numbers)
    for i in range(1,len(numbers)+1):
        nums=list(itertools.permutations(number,i))
        for num in nums:
            new_num=''.join(num)
            if new_num[0]=='0':
                continue
            if isPrime(int(new_num)):
                if new_num not in prime:
                    prime.append(new_num)
    return len(prime)

def isPrime(num):
    if num<2:
        return False
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True