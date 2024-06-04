from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    queue = deque([(x, 0)])
    visited = set([x])
    
    while queue:
        cur_num, steps = queue.popleft()
        
        if cur_num == y:
            return steps
        
        
        
        for next_num in (cur_num + n, cur_num * 2, cur_num * 3):
            if next_num <= y and next_num not in visited:
                visited.add(next_num)
                queue.append([next_num, steps + 1])
                
    return -1