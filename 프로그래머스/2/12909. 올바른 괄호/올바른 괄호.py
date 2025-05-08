def solution(s):
    st = []
    
    for parentheses in s:
        # 열린 괄호일 경우
        if parentheses == '(':
            st.append('(')
        
        # 닫힌 괄호일 경우
        else:
            # 괄호가 짝지어져 있는 경우
            if st and st[-1] == '(':
                st.pop()
            # 괄호가 짝지어져 있는 경우 == 올바르지 않은 괄호
            else:
                return False
    
    # 반복문 끝났는데 아직 스택에 괄호가 남은 경우 == 올바르지 않은 괄호
    if st:
        return False
    
    return True