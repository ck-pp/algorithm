import sys
import heapq

V, E = map(int, sys.stdin.readline().split())  # 정점 개수, 간선 개수
K = int(sys.stdin.readline())  # 시작 정점
u_v_w = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]

g = [[] for _ in range(V+1)]


for u, v, w in u_v_w:
    g[u].append((v, w))  # (도착점, 가중치)
    
distance = [float("inf")] * (V+1)
distance[K] = 0  # 시작점

# 우선순위 큐(min-heap) 사용
q = [(0, K)]  # 거리, 정점

while q:
    cur_dist, cur_node = heapq.heappop(q)
    
    # 이미 더 비용 적은 경로 알고 있는 경우 무시
    if cur_dist > distance[cur_node]:
        continue
    
    # 연결된 노드 검사
    for neighbor, w in g[cur_node]:
        dist_via_cur = cur_dist + w
        
        if dist_via_cur < distance[neighbor]:
            distance[neighbor] = dist_via_cur
            heapq.heappush(q, (dist_via_cur, neighbor))
            
for i in range(1, len(distance)):
    print("INF" if distance[i] == float("inf") else distance[i])