import math
def solution(n, m, section):
    cnt = 0
    i = 1
    length = len(section)
    while i <= length:
        j = i+1
        if i < length:
            while j <= length and section[-i] - section[-j] +1 <= m:
                j += 1
            cnt += 1
            i = j
        else:
            cnt += 1
            i += 1
    return cnt