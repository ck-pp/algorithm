def solution(rsp):
    ans = ''
    win = {'0': '5', '2': '0', '5': '2'}
    for i in rsp:
        ans += win[i]
    return ans