def solution(s):
    stack = []  # 스택 초기화
    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
            
    if stack:
        return 0
    
    return 1