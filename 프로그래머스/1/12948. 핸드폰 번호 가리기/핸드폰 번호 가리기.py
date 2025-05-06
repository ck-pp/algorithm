def solution(phone_number):
    n = len(phone_number) - 4  # *으로 가릴 문자열 길이
    
    return '*' * n + phone_number[n:]