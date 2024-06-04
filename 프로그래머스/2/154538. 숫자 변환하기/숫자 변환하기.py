from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    queue = deque([(y, 0)])
    visited = set([y])
    
    while queue:
        cur_num, steps = queue.popleft()
        
        if cur_num == x:
            return steps
        
        c_nums = [cur_num - n]
        if cur_num % 2 == 0:
            c_nums.append(cur_num // 2)
        if cur_num % 3 == 0:
            c_nums.append(cur_num // 3)
            
        for next_num in c_nums:
            if next_num >= x and next_num not in visited:
                visited.add(next_num)
                queue.append([next_num, steps + 1])
                
    return -1