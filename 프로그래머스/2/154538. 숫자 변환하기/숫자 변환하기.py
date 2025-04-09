from collections import deque

def solution(x, y, n):
    # 연산 범위 줄이기 위해 y -> x로 찾는다. (나머지 == 0으로 조건 체크)
    q = deque([(y, 0)])  # (현재 값, 연산 횟수)
    visited = set([y])
    
    # bfs 로직 실행 (최소 연산 횟수)
    while q:
        cur_num, steps = q.popleft()
        
        if cur_num == x:
            return steps
            
        possible_nums = []
        # 문제에서 주어진 조건을 여기서 체크
        if cur_num - n > 0 :
            possible_nums.append(cur_num - n)
        if cur_num % 2 == 0 :
            possible_nums.append(cur_num // 2)
        if cur_num % 3 == 0:
            possible_nums.append(cur_num // 3)
            
        for next_num in possible_nums:
            if next_num not in visited :
                q.append((next_num, steps + 1))
                visited.add(next_num)
                
    return -1