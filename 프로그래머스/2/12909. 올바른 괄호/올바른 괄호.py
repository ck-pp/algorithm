def solution(s):
    stack = []
    n = len(s)
    
    for i in range(n):
        if s[i] == '(':  # 열린 괄호인 경우
            stack.append(s[i])
        else:  # 닫힌 괄호인 경우
            if not stack or stack[-1] != '(':  # 올바르지 않은 괄호
                return False
            else:
                stack.pop()
    
    if stack: return False  # 열린 괄호만 남음(= 올바르지 않은 괄호)
    else: return True  # 올바른 괄호