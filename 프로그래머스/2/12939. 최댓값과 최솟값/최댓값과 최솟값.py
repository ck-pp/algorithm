def solution(s):
    s_nums = list(map(int, s.split()))
    
    return str(min(s_nums)) + ' ' + str(max(s_nums))