def solution(n):
    rev_ternary = ''
    while n > 0:
        n, mod = divmod(n, 3)  # n을 3으로 나눈 몫과 나머지
        rev_ternary += str(mod)
        
    return int(rev_ternary, 3)