def solution(a, b):
    ans = 0
    max_v, min_v = max(a, b), min(a, b)
    for i in range(min_v, max_v+1):
        ans += i
    return ans