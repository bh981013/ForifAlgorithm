
def solution(N, number):
    cache = [-1 for _ in range(3200000)]
    arr = [[] for _ in range(9)]
    arr[1].append(N)
    cache[N] = 1
    if N == number: return 1
    for i in range(2, 9):
        a = 1
        b = i-a
        temp = [int(str(N)*i)]
        while(a<=i//2):
            # print(f"a:{a}, b:{b}")
            for A in arr[a]:
                for B in arr[b]:
                    # print(f"A:{A}, B:{B}")
                    temp +=[A+B, A-B,A*B, B-A, A//B, B//A]
            a+=1
            b-=1
        # print(temp)
        for t in temp:
            if 0<t<3200000 and cache[t] == -1:
                # print(t, i)
                arr[i].append(t)
                cache[t] = i
            if t==number:
                return i
    return -1
