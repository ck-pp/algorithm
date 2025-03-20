import sys
from collections import deque
input = sys.stdin.readline

# 세로 길이, 가로 길이, 음식물 쓰레기의 개수
N, M, K = map(int, input().split())
food_wastes = [tuple(map(int, input().split())) for _ in range(K)]

# 쓰레기 영역 표시(1)
g = [[0] * M for _ in range(N)]
for y, x in food_wastes:
    g[y - 1][x - 1] = 1  # 좌표 0부터 시작하도록 맞춤
    
# 1. bfs 정의
def bfs(g, q, visited, start):
    dpos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 이동 가능한 좌표
    cur_size = 1  # 현재 쓰레기 크기

    while q:
        cur_pos = q.popleft()
        
        for dx, dy in dpos:
            nx, ny = cur_pos[1] + dx, cur_pos[0] + dy
            
            # len(g[0]) : 가로 길이(M), len(g) : 세로 길이(N)
            if 0 <= nx < len(g[0]) and 0 <= ny < len(g):
                if (ny, nx) not in visited:
                    if g[ny][nx] == 1:
                        cur_size += 1
                        q.append((ny, nx))
                        visited.add((ny, nx))
        
    return cur_size

# 2. 음식물 쓰레기 영역 중에 방문하지 않은 좌표에서 bfs 호출
visited = set([])
ans = []
for i in range(N):
    for j in range(M):
        if g[i][j] == 1 and (i, j) not in visited:
            visited.add((i, j))
            q = deque([(i, j)])  # 현재 좌표
            ans.append(bfs(g, q, visited, (i, j)))
            

# 음식물 중 가장 큰 음식물의 크기 출력
print(max(ans))