def solution(my_string, m, c):
    res = [my_string[n : n + m] for n in range(0, len(my_string) - m + 1, m)]
    
    return ''.join([str[c - 1] for str in res])