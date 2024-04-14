def solution(s):
    list = s.split(' ')
    ans = []
    for i in list:
        ans.append(int(i))
    return str(min(ans)) + ' ' + str(max(ans))