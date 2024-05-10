from collections import deque

def solution(order):
    ans = 0
    pos = 0
    st = deque([i+1 for i in range(len(order))])
    temp_st = []
    order = deque(order)
    while order:
        o = order[0]
        if (st and o != st[0]) or not st: 
            if temp_st and temp_st[-1] == o:
                temp_st.pop()
                order.popleft()
                ans += 1
            else:
                if st:
                    temp_st.append(st.popleft())
                else:
                    break
        else:
            st.popleft()
            order.popleft()
            ans += 1
                
    return ans