def solution(n):
    i = 0
    ans = 0
    while i < n:
        i += 1
        ans += 1
        if ans % 3 == 0 or str(ans).find('3') > -1:
            i -= 1
    return ans