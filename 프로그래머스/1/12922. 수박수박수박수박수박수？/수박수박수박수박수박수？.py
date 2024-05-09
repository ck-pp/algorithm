def solution(n):
    ans = ''
    dict = {0:'박', 1:'수'}
    for i in range(n):
        ans += dict[(i+1)%2]
    return ans