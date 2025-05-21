def solution(s):
    ans = []
    words = s.upper().split(' ')
    
    for i in range(len(words)):
        n = len(words[i])
        word = ''
        for j in range(n):
            # 짝수번째 알파벳 = 인덱스가 홀수인 알파벳
            if j % 2 == 1:
                word += words[i][j].lower()
            # 홀수번째 알파벳 = 인덱스가 짝수인 알파벳
            else:
                word += words[i][j]
        
        ans.append(word)
        
    return ' '.join(ans)