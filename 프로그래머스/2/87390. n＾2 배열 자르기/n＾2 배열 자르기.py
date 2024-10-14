def solution(n, left, right):
    ans_arr = []
    for i in range(left, right + 1):
        ans_arr.append(max(i // n, i % n) + 1)
        
    return ans_arr