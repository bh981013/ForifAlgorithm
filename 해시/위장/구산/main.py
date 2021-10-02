
def solution(clothes):
    clothes_hidden = {}
    for cloth in clothes:
        if cloth[1] in clothes_hidden.keys():
            clothes_hidden[cloth[1]] += 1
        else:
            clothes_hidden[cloth[1]] = 1
    answer = 1
    for i in clothes_hidden.values():
        answer *= (i+1)
    return answer - 1

# clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["sunglass", "face"], ["glasses", "face"], ["blue_tshirt", "shirt"], ["jeans", "pants"],
           ["long_coat", "coat"]]
print(solution(clothes))
