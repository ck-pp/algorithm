import sys
from collections import deque

def bfs(g, visited, position):
    q = deque([position])
    visited.add(position)  # 시작 위치 좌표
    dpos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        cur_x, cur_y = q.popleft()
        
        for dx, dy in dpos:
            next_x, next_y = cur_x + dx, cur_y + dy
            if 0 <= next_x < M and 0 <= next_y < N:
                if (next_x, next_y) not in visited and g[next_y][next_x] == 1:
                    q.append((next_x, next_y))
                    visited.add((next_x, next_y))

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    xy_positions = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]
    # 0: 빈 땅, 1: 배추 땅
    
    g = [[0] * M for _ in range(N)]
    for x, y in xy_positions:
        g[y][x] = 1  # 배추 심어져 있는 땅
    
    visited = set()
    cnt = 0
    for pos in xy_positions:
        if pos not in visited:
            bfs(g, visited, pos)
            cnt += 1  # 필요한 최소의 배추흰지렁이 마리 수
    
    print(cnt)