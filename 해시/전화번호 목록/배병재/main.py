def solution(phone_book):
    dict={}
    phone_book.sort(key=lambda x:len(x))
    for phone in phone_book:
        str=""
        for p in phone:
            str+=p
            if dict.get(str):
                return False
            elif str==phone:
                dict[str]=1
    return True
