import sys
import heapq
# 벽보다 빈 방을 먼저 탐색해야 하므로 우선순위 큐 사용(= 다익스트라?)
input = sys.stdin.readline

M, N = map(int, input().split())  # 가로 크기, 세로 크기(N*M)
rooms = [list(map(int, input().strip())) for _ in range(N)]

# (1, 1) -> (N, M) 대신 (0, 0) -> (N-1, M-1)
dpos = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = [(0, 0, 0)]  # 벽부순횟수, x좌표, y좌표
visited = [[False] * M for _ in range(N)]

while q:
    cnt, x, y = heapq.heappop(q)
    
    if (x, y) == (N-1, M-1):
        print(cnt)
        break
    
    # 방문 처리
    if visited[x][y]:
        continue
    visited[x][y] = True
    
    for dx, dy in dpos:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y]:
            if rooms[next_x][next_y] == 1:
                heapq.heappush(q, (cnt + 1, next_x, next_y))
            else:
                heapq.heappush(q, (cnt, next_x, next_y))