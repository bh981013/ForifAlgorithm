def solution(brown, yellow):
    answer = []
    S = brown + yellow
    for i in range(1, int(S**1/2)+1):
        if S % i == 0:
            a = i
            b = S / i
            if (a-2) * (b-2) == yellow and 2*a + 2*b -4 == brown:
                return [b, a]