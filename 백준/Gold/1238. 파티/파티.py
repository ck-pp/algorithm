import sys
from collections import deque

def dijkstra(distance, start, g):
    q = deque([(0, start)]) # (소요시간, 현재 마을)
    
    while q:
        cur_dist, cur_node = q.popleft()
    
        # 이미 더 짧은 경로가 있다면 패스
        if cur_dist > distance[cur_node]:
            continue
    
        for neighbor, time in g[cur_node]:
            dist_via_cur = cur_dist + time
        
            if dist_via_cur < distance[neighbor]:
                distance[neighbor] = dist_via_cur
                q.append((dist_via_cur, neighbor))

N, M, X = map(int, sys.stdin.readline().split())
road_infos = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

g = [[] for _ in range(N + 1)]
for u, v, t in road_infos:
    g[u].append((v, t))
    
from_X_distance = [float('inf')] * (N + 1)
from_X_distance[X] = 0  # 시작점
to_X_distance = [0 for _ in range(N + 1)]  # 이게 플루이드워셜인가..
q = deque([(0, X)])  # (소요시간, 현재 마을)

# 각 마을에서 X까지 가는 최단 경로
for i in range(1, N+1):
    distance = [float('inf')] * (N + 1)
    distance[i] = 0
    
    dijkstra(distance, i, g)
    to_X_distance[i] = distance[X]   

# X에서 각 마을까지 가는 최단 경로
dijkstra(from_X_distance, X, g)

ans = -1
# X까지 갔다오는 시간이 가장 큰 학생의 소요시간 출력
for to_time, from_time in zip(to_X_distance, from_X_distance):
    if to_time + from_time != float('inf'):
        ans = max(ans, to_time + from_time)

print(ans)