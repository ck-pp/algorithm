import sys
from collections import deque

def bfs(maps, visited, start_pos):
    q = deque([start_pos])
    visited.add(start_pos)
    dpos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cnt = 1  # 현재 위치에 집이 있으므로 1부터 시작
    
    while q:
        cur_pos = q.popleft()
        
        for d in dpos:
            next_x, next_y = cur_pos[0] + d[0], cur_pos[1] + d[1]
            # 지도 범위 안에 있으며, 집이 있고, 방문하지 않은 경우에만 큐에 추가
            if 0 <= next_x < N and 0 <= next_y < N and maps[next_y][next_x] == 1:
                if (next_x, next_y) not in visited:
                    q.append((next_x, next_y))
                    visited.add((next_x, next_y))
                    cnt += 1  # 집이 연결되어 있는 경우에만 카운트 증가
                    
    return cnt

N = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

visited = set()
house_cnts = []

for i in range(N):
    for j in range(N):
        if (i, j) not in visited and maps[j][i] == 1:  # 방문하지 않았고 집이 있는 경우에만 탐색
            house_cnts.append(bfs(maps, visited, (i, j)))

house_cnts.sort()
print(len(house_cnts))  # 총 단지 수 출력
for cnt in house_cnts:
    print(cnt)