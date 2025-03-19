import sys
import heapq
input = sys.stdin.readline

n = int(input())
rooms = [list(map(int, list(input().strip()))) for _ in range(n)]

distance = [[float('INF')] * n for _ in range(n)]
distance[0][0] = 0

# 우선순위 큐 (min-heap) 사용
q = [(0, (0, 0))]  # (거리, 현재 좌표)

dpos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    cur_dist, cur_pos = heapq.heappop(q)
    
    # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if distance[cur_pos[0]][cur_pos[1]] < cur_dist:
        continue
    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for dx, dy in dpos:
        nx, ny = cur_pos[1] + dx, cur_pos[0] + dy
        if 0 <= nx < n and 0 <= ny < n:
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            dist_via_cur = cur_dist + (1 - rooms[ny][nx])  # 흰 방(1)이면 가중치 0, 검은 방(0)이면 가중치 1
            if dist_via_cur < distance[ny][nx]:
                distance[ny][nx] = dist_via_cur
                heapq.heappush(q, (dist_via_cur, (ny, nx)))
    
# 3. 흰 방으로 바꾸어야 할 최소의 검은 방의 수 출력
print(distance[n-1][n-1])