def solution(s):
    n = len(s)
    
    # 문자열 길이가 짝수일 경우
    if n % 2 == 0:
        return s[n // 2 - 1] + s[n // 2]
    # 문자열 길이가 홀수일 경우
    else:
        return s[n // 2]