def solution(my_string, n):
    ans = ''
    for s in my_string:
        ans += s * n
    return ans