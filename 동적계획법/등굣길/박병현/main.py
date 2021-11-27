cache = []
maxnum = 1000000007
def dp(h, w):
    global cache
    if cache[h][w] != -1:
        return cache[h][w]
    if h>1 and w>1:
        cache[h][w] = ((dp(h-1, w)+dp(h, w-1))) % maxnum
    elif h == 1 and w>1:
        cache[h][w] = dp(h, w-1)
    elif w == 1 and h > 1:
        cache[h][w] = dp(h-1, w)
    return cache[h][w]

def solution(m, n, puddles):
    global cache
    cache = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    cache[1][1] = 1
    for m_, n_ in puddles:
        cache[n_][m_] = maxnum
    dp(n,m)
    answer = cache[n][m]
    return answer

# print(solution(4,3,[[2, 2]]))
# print("\n".join(map(str,cache)))