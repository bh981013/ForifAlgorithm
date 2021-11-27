cache = []
def dp(h,w,tri):
    global cache
    if cache[h][w] != -1:
        return cache[h][w]
    if h==0:
        cache[h][w] = tri[h][w]
        return tri[h][w]
    if 0<w<len(cache[h])-1:
        cache[h][w] = max(dp(h-1,w, tri), dp(h-1,w-1, tri)) + tri[h][w]
    elif w == 0:
        cache[h][w] = dp(h-1,w, tri) + tri[h][w]
    else:
        cache[h][w] = dp(h-1,w-1, tri) + tri[h][w]
    return cache[h][w]

def solution(triangle):
    global cache
    cache = [[-1 for _ in range(i+1)] for i in range(len(triangle))]
    for i in range(len(triangle)):
        dp(len(triangle)-1, i, triangle)
    answer = max(cache[len(triangle)-1])    
    return answer