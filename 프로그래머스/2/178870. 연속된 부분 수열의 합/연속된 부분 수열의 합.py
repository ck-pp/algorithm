from collections import deque

def solution(sequence, k):
    ans = []
    i = len(sequence)-1
    st = deque([])
    sum_s = 0
    while i > -1:
        st.append(i)
        sum_s += sequence[i]
        if sum_s >= k and (not ans or ans[-1][1]-ans[-1][0] >= st[0]-st[-1]):
            if sum_s == k:
                ans.append([st[-1], st[0]])
            i = st[-1] -1
            sum_s -= sequence[st[0]]
            st.popleft()
        else:
            i -= 1
    return ans[-1]