import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())  # 세로 길이 n, 가로 길이 m
painting_infos = [list(map(int , input().split())) for _ in range(n)]

def bfs(x, y, visited):
    # 4방향 탐색
    dpos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque([(x, y)])
    area = 1  # 현재 시작점 포함
    
    while q:
        cur_x, cur_y = q.popleft()

        for dx, dy in dpos:
            next_x, next_y = cur_x + dx, cur_y + dy
            
            # 범위 체크 및 방문 여부 확인
            if 0 <= next_y < n and 0 <= next_x < m:
                if painting_infos[next_y][next_x] == 1 and (next_x, next_y) not in visited:
                    q.append(((next_x, next_y)))
                    visited.add((next_x, next_y))
                    area += 1
    
    return area

visited = set()
num_paintings = 0
max_area = 0
      
# 전체 탐색
for i in range(n):
    for j in range(m):
        if painting_infos[i][j] != 0 and (j, i) not in visited:
            num_paintings += 1
            visited.add((j, i))
            max_area = max(max_area, bfs(j, i, visited))
            
print(num_paintings)  # 그림의 개수
print(max_area)  # 가장 넓은 그림의 넓이