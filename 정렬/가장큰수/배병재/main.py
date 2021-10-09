def solution(numbers):
    new_nums=list(map(str,numbers))
    new_nums.sort(key=lambda x:x*3,reverse=True)
    return str(int(''.join(new_nums)))