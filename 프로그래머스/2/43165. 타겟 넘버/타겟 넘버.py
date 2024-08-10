from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)]) # 현재 인덱스, 합
    cnt = 0
    
    while queue:
        idx, cur_sum = queue.popleft()
        
        if idx == len(numbers):
            if cur_sum == target:
                cnt += 1
        else:
            queue.append((idx + 1, cur_sum - numbers[idx]))
            queue.append((idx + 1, cur_sum + numbers[idx]))
            
    return cnt