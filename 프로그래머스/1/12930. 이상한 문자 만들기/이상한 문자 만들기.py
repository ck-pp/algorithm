def solution(s):
    ans = ''
    words = s.upper().split(' ')
    
    for word in words:
        n = len(word)

        for i in range(n):
            # 짝수번째 알파벳 == 인덱스가 홀수인 알파벳
            if i % 2 == 1:
                ans += word[i].lower()
            # 홀수번째 알파벳 == 인덱스가 짝수인 알파벳
            else:
                ans += word[i]
        
        ans += ' '
        
    return ans[:-1]