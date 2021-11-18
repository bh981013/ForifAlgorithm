def solution(numbers):
    answer = ''
    arr = []
    d = [0 for _ in range(4)]
    d[1] = 5
    d[2] = 2
    d[3] = 1
    is0, is1000 = 0,0
    for n in numbers:
        if n==0:
            is0 +=1
        elif n==1000:
            is1000 += 1
        else:
            restlen = d[len(str(n))]
            arr.append([str(n) + str(n) * restlen, len(str(n))])
    arr.sort(key = lambda x: x[0], reverse = True)
    for a in arr:
        num = a[0][:a[1]]
        answer += num
    answer+= "1000" * is1000
    answer += "0" * is0
    while(answer and answer[0] == "0"):
        answer = answer[1:]
    if not answer:
        answer = "0"
    return answer