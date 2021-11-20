def solution(n, times):
    left=0
    answer=right=max(times)*n
    while left<=right:
        mid=(left+right)//2
        people=0
        for time in times:
            people+=mid//time
        if people<n:
            left=mid+1
        else:
            right=mid-1
            answer=min(answer,mid)
    return answer