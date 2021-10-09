def solution(citations):
    h_idx=0
    citations.sort()
    for i in range(1,len(citations)+1):
        cnt=0
        for j in citations:
            if cnt>i:
                break
            elif j>=i:
                cnt+=1
        if cnt>=i:
            h_idx=i
    print(h_idx)
    return h_idx