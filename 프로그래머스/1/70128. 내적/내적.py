def solution(a, b):
    ans = 0
    for a_e, b_e in zip(a, b):
        ans += a_e*b_e
    return ans