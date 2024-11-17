import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    l = int(input())  # 체스판: (0~l-1, 0~l-1)
    start_x, start_y = map(int, input().split())  # 현재 나이트가 있는 칸
    end_x, end_y = map(int, input().split())  # 나이트가 이동할 칸
    
    # 한번에 이동 가능한 칸
    dpos = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    q = deque([(0, (start_x, start_y))])  # 시작칸
    visited = set([(start_x, start_y)])
    
    while q:
        steps, cur_pos = q.popleft()
        
        if cur_pos == (end_x, end_y):
            break
        
        for dx, dy in dpos:
            next_x, next_y = cur_pos[0] + dx, cur_pos[1] + dy
            if 0 <= next_x < l and 0 <= next_y < l and (next_x, next_y) not in visited:
                q.append((steps + 1, (next_x, next_y)))
                visited.add((next_x, next_y))
                
    print(steps)