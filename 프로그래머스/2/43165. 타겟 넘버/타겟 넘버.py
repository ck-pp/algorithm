from collections import deque

def solution(numbers, target):
    q = deque([(0, 0)])
    cnt = 0
    
    while q:
        idx, cur_num = q.popleft()
        
        if idx == len(numbers):
            if cur_num == target:
                cnt += 1
        else:
            q.append((idx + 1, cur_num + numbers[idx]))
            q.append((idx + 1, cur_num - numbers[idx]))
        
    return cnt