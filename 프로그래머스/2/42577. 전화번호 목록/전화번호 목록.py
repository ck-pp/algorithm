def solution(phone_book):
    # 한 번호가 다른 번호의 접두어인 경우 있는지 확인
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    
    return True