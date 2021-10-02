def solution(priorities, location):
    arr=[]
    ans=1
    for idx,i in enumerate(priorities):
        arr.append((idx,i))
    while True:
        top=priorities.pop(0)
        doc=arr.pop(0)
        if len(priorities)==0:
            break
        if top<max(priorities):
            priorities.append(top)
            arr.append(doc)
        elif doc[0]==location:
            break
        else:
            ans+=1
    return ans
