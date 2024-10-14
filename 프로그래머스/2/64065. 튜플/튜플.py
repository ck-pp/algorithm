def solution(s):
    # 튜플 : 중복, 순서
    res = []
    s = s[1:len(s)-2].replace('{', '').split('},')
    sort_s = sorted(s, key=len)
    for s in sort_s:
        for ch_num in s.split(','):
            num = int(ch_num)
            if num not in res:
                res.append(num)
                
    return res