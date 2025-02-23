def solution(s):
    # 모두 소문자로 바꾼 뒤, 맨 앞글자만 대문자로 변환
    s = s.lower().title()
    n = len(s)
    ans = ''
    for i in range(n):
        # 현재 맨 앞이 숫자일 경우 그 뒤 문자가 대문자로 변환되어 있기 때문에 이 경우에 다시 소문자로 변환한다.
        if s[i-1].isnumeric() and s[i].isalpha():
            ans += s[i].lower()
        else:
            ans += s[i]
    
    return ans