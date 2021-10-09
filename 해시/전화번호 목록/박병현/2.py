def solution(phone_book):
    d = {}
    phone_book.sort(key=len)
    for p in phone_book:
        num = ""
        for n in p:
            num += n
            if d.get(num):
                return False
        d[num] = True
    return True