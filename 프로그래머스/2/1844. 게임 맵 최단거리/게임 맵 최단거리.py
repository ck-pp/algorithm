from collections import deque

def solution(maps):
    q = deque([(1, (1, 1))])  # 이동 횟수, 좌표
    visited = set((1, 1))
    move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    n, m = len(maps), len(maps[0])
    
    while q:
        steps, cur_pos = q.popleft()
        
        if cur_pos == (n, m):
            return steps
        
        move_pos = []
        for dy, dx in move:
            y, x = cur_pos[0] + dy, cur_pos[1] + dx
            if 0 < y <= n and 0 < x <= m and maps[y-1][x-1] > 0:
                move_pos.append((y, x))
            
        for next_pos in move_pos:
            if next_pos not in visited:
                q.append((steps + 1, next_pos))
                visited.add(next_pos)
    
    return -1