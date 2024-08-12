def solution(num, k): 
    idx = str(num).find(str(k))
    return idx if idx < 0 else idx + 1