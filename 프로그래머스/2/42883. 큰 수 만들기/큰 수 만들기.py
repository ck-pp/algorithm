def solution(number, k):
    st = []
    for num in number:
        while st and st[-1] < num and k > 0:
            st.pop()
            k -= 1
        st.append(num)
    
    # 만약 제거해야 할 숫자가 남아 있다면, 뒤에서부터 제거
    while k > 0:
        st.pop()
        k -= 1
    
    return ''.join(st)