def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: len(x))
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if phone_book[i] != phone_book[j] and phone_book[i].startswith(phone_book[j]):
                return False
    return True

phone_book = ["123456789123456789","23456789"]
print(solution(phone_book))