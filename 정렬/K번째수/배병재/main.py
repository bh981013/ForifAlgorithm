def solution(array, commands):
    answer = []
    for idx,command in enumerate(commands):
        arr=[]
        i=command[0]
        j=command[1]
        k=command[2]
        for ind in range(i-1,j):
            arr.append(array[ind])
        arr.sort()
        answer.append(arr[k-1])
    return answer