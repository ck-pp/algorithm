from collections import deque

def solution(x, y, n):
    
    queue = deque([[0, y]])
    visited = set([y])
    
    while queue:
        cnt, cur_sum = queue.popleft()
        
        if cur_sum == x:
            return cnt
        
        num_list = []
        if cur_sum - n >= x:
            num_list.append(cur_sum - n)
        if cur_sum % 2 == 0:
            num_list.append(cur_sum // 2)
        if cur_sum % 3 == 0:
            num_list.append(cur_sum // 3)
            
        for next_num in num_list:
            if next_num not in visited:
                queue.append([cnt + 1, next_num])
                visited.add(next_num)
    
    return -1