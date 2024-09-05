from collections import deque

def solution(x, y, n):
    q = deque([(y, 0)])  # (값, 연산 횟수)
    
    if y == x:
        return 0
    
    while q:
        cur_val, steps = q.popleft()
        
        if cur_val == x:
            return steps
        
        val_list = []
        if cur_val - n > 0:
            val_list.append(cur_val - n)
        if cur_val % 2 == 0:
            val_list.append(cur_val // 2)
        if cur_val % 3 == 0:
            val_list.append(cur_val // 3)
        
        for next_val in val_list:
            q.append((next_val, steps + 1))

    return -1