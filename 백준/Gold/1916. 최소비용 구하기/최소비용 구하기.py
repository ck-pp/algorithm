import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
# [출발 도시 번호, 도착 도시 번호, 버스 비용]
bus_infos = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
start, end = map(int, sys.stdin.readline().split())

g = [[] for _ in range(N + 1)]
for s, e, w in bus_infos:
    # 한 방향 그래프
    g[s].append((e, w))  # (도착번호, 비용)
    
distance = [float('inf')] * (N + 1)
distance[start] = 0  # 시작점

# 우선순위 큐(min-heap) 사용
q = [(0, start)]  # (거리, 도시)

while q:
    cur_dist, cur_city = heapq.heappop(q)
    
    # 이미 더 비용 적은 경로 알고 있는 경우 무시
    if cur_dist > distance[cur_city]:
        continue
    
    # 현재 노드와 연결된 다른 노드 검사
    for neighbor, weight in g[cur_city]:
        dist_via_cur = cur_dist + weight
        
        # 더 비용 적은 경로 찾은 경우 갱신
        if dist_via_cur < distance[neighbor]:
            distance[neighbor] = dist_via_cur
            heapq.heappush(q, (dist_via_cur, neighbor))

print(distance[end])