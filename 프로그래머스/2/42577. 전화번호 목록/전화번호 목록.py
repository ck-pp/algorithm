def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        cur_n = len(phone_book[i])
        next_n = len(phone_book[i+1])
        # 정렬을 했기 때문에 바로 다음 문자열과만 비교
        if cur_n <= next_n and phone_book[i] == phone_book[i+1][:cur_n]:
            return False
    
    return True