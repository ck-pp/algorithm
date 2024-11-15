import sys
import heapq

input = sys.stdin.readline

N, M, K, X = map(int, input().split())  # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
A_B_lists = [list(map(int, input().split())) for _ in range(M)]

g = [[] for _ in range(N + 1)]
for A, B in A_B_lists:
    g[A].append((B, 1))  # A-B 모든 거리 1
    
q = [(0, X)]  # (거리, 시작 도시)
distance = [float('inf')] * (N + 1)  # X로부터 거리
distance[X] = 0

while q:
    cur_dist, cur_city = heapq.heappop(q)
    
    # 더 짧은 경로가 이미 있는 경우
    if cur_dist > distance[cur_city]:
        continue
    
    for neighbor, weight in g[cur_city]:
        dist_via_cur = distance[cur_city] + weight
        if dist_via_cur < distance[neighbor]:  # 더 짧은 경로 발견한 경우, 업데이트
            heapq.heappush(q, (dist_via_cur, neighbor))
            distance[neighbor] = dist_via_cur

isEmpty = True
for idx in range(len(distance)):
    if distance[idx] == K:
        isEmpty = False
        print(idx)

if isEmpty:  # 최단 거리가 K인 도시가 하나도 없는 경우
    print(-1)