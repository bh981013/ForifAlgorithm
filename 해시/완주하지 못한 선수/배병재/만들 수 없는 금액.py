n=map(int,input())
arr=list(map(int,input().split()))
arr.sort()

'''
    target을 기준으로 만들 수 있는지 여부파악이 중요하다
'''

target=1

for i in arr:
    if target<i:
        break
    target+=i

print(target)
