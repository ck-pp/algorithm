from collections import deque

def solution(bridge_length, weight, truck_weights):
    ans = 0
    temp_st = deque([0] * bridge_length)
    truck_w = deque(truck_weights)
    sum_s = sum(temp_st)
    
    while truck_w:
        ans += 1
        sum_s -= temp_st.popleft()
        if sum_s + truck_w[0] <= weight:
            temp_st.append(truck_w.popleft())
            sum_s += temp_st[-1]
        else:
            temp_st.append(0)
            
    return ans + bridge_length