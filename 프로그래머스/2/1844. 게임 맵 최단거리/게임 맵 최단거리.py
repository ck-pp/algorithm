from collections import deque

def solution(maps):
    queue = deque([(1, (1, 1))]) # 이동 칸 수, 현재 좌표
    visited = set([(1, 1)]) # 좌표
    d_pos = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    n, m = len(maps), len(maps[0])
    
    while queue:
        steps, cur_pos = queue.popleft()
        
        if cur_pos == (n, m):
            return steps
        
        for dx, dy in d_pos:
            next_x, next_y = dx + cur_pos[0], dy + cur_pos[1]
            if (1 <= next_x <= n) and (1 <= next_y <= m) and (next_x, next_y) not in visited and maps[next_x-1][next_y-1] == 1:        
                queue.append((steps + 1, (next_x, next_y)))
                visited.add((next_x, next_y))
        
    return -1