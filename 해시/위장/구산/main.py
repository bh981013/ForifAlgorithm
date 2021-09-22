def get_result(clothes, clothes_hidden, end):
    result = 0
    if end:
        return 0

    for i in range(len(clothes)):
        end = (i == len(clothes) - 1)
        if clothes[i][1] not in clothes_hidden:
            clothes_hidden.append(clothes[i][1])
            result += 1
            temp = clothes.copy()
            temp.remove(temp[i])
            result += get_result(temp, clothes_hidden, end)
            clothes_hidden.remove(clothes[i][1])
    return result


def solution(clothes):
    clothes_hidden = []
    return get_result(clothes, clothes_hidden, False)

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["sunglass", "face"], ["glasses", "face"], ["blue_tshirt", "shirt"], ["jeans", "pants"],
#            ["long_coat", "coat"]]
print(solution(clothes))
