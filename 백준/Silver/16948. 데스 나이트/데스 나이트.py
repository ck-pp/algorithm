import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
r1, c1, r2, c2 = map(int, input().split())  # 시작 좌표, 도착 좌표

# 1. bfs 정의
def bfs(start, end):
    # 이동 가능한 좌표
    dpos = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
    q = deque([(start, 0)])  # (좌표, 이동 횟수)
    visited = set([start])  # 방문 여부 체크
    
    while q:
        cur_position, steps = q.popleft()
        
        # 도착 좌표일 경우 이동 횟수 반환
        if cur_position == end:
            return steps
        
        for dx, dy in dpos:
            next_x, next_y = cur_position[0] + dx, cur_position[1] + dy
            
            # 이동할 수 있는 좌표
            if 0 <= next_x < n and 0 <= next_y < n:
                if (next_x, next_y) not in visited:
                    q.append(((next_x, next_y), steps + 1))
                    visited.add((next_x, next_y))
        
    return -1

# 2. 최소 이동 횟수 출력
print(bfs((r1, c1), (r2, c2)))