from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([((1, 1), 1)]) # xy좌표, 이동 칸 수 1부터 시작 (시작지점도 포함이므로!)
    visited = set([(1, 1)])
    
    while queue:
        cur_xy, steps = queue.popleft()
        cur_x, cur_y = cur_xy

        if cur_xy == (n, m):
            return steps
        
        c_xy = []
        if cur_x > 1:
            c_xy.append((cur_x-1, cur_y))
        if cur_x < n:
            c_xy.append((cur_x+1, cur_y))
        if cur_y > 1:
            c_xy.append((cur_x, cur_y-1))
        if cur_y < m:
            c_xy.append((cur_x, cur_y+1))
            
        for next_xy in c_xy:
            if maps[next_xy[0]-1][next_xy[1]-1] != 0 and next_xy not in visited:
                visited.add(next_xy)
                queue.append((next_xy, steps + 1))
                
    return -1