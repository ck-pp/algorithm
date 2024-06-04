from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([((0, 0), 1)]) # xy좌표, 이동 칸 수 1부터 시작(시작지점도 포함이므로!)
    visited = set([(0, 0)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 방향
    
    while queue:
        (cur_x, cur_y), steps = queue.popleft()

        if (cur_x, cur_y) == (n-1, m-1):
            return steps
            
        for dx, dy in directions:
            next_x, next_y = cur_x + dx, cur_y + dy
            
            if (0 <= next_x < n and 0 <= next_y < m) and maps[next_x][next_y] == 1 and (next_x, next_y) not in visited:
                visited.add((next_x, next_y))
                queue.append(((next_x, next_y), steps + 1))
                
    return -1