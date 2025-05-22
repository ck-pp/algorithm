from collections import deque
def solution(s):
    i = 0
    stack = []  # 스택 초기화
    while i < len(s):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    
        i += 1
        
    # 스택에 값이 남아있는 경우 == 모두 짝지어 제거 불가능
    if stack:
        return 0
    # 스택에 값이 남아있지 않은 경우 == 모두 짝지어 제거 가능
    else:
        return 1