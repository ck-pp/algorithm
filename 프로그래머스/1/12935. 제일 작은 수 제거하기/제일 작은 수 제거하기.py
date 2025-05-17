def solution(arr):
    n = len(arr)
    if n == 1:
        return [-1]
    # remove: 값으로 제거, del: 인덱스로 제거
    arr.remove(min(arr))
    
    return arr