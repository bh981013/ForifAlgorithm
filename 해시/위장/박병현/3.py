def solution(clothes):
    d = {}
    for name, kind in clothes:
        if d.get(kind):
            d[kind] += 1
        else:
            d[kind] = 1
    res = 1
    for v in d.values():
        res *= (v+1)
    res -= 1
    return res