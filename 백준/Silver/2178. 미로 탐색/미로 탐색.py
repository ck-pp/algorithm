import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
roads = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
# (0, 0) -> (N-1, M-1)

q = deque([(1, (0, 0))])  #(지난 칸 수, 현재 좌표)
visited = set([(0, 0)])
dpos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    steps, cur_pos = q.popleft()
    
    if cur_pos == (N-1, M-1):
        break
    
    for dx, dy in dpos:
        next_x, next_y = cur_pos[0] + dx, cur_pos[1] + dy
        if 0 <= next_x < N and 0 <= next_y < M:
            if (next_x, next_y) not in visited and roads[next_x][next_y] == 1:
                q.append((steps + 1, (next_x, next_y)))
                visited.add((next_x, next_y))
    
print(steps)