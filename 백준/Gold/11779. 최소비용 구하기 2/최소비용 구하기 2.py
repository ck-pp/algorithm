import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
bus_infos = [list(map(int,input().split())) for _ in range(m)]
start, end = map(int, input().split())

g = [[] for _ in range(n + 1)]
for u, v, w in bus_infos:
    g[u].append((v, w))

distance = [float('inf')] * (n + 1)
prev_city = [-1] * (n + 1)  # 역추적위해 각 도시로 오기 전의 도시 저장
distance[start] = 0  # 출발지

q = [(0, start)]  # (거리, 도시)

while q:
    cur_dist, cur_city = heapq.heappop(q)
    
    # 이미 더 짧은 경로 있을 경우
    if cur_dist > distance[cur_city]:
        continue
    
    # 거리 비교
    for neighbor, weight in g[cur_city]:
        dist_via_cur = cur_dist + weight
        
        # 더 짧은 경로가 있는 경우 갱신
        if dist_via_cur < distance[neighbor]:
            distance[neighbor] = dist_via_cur
            prev_city[neighbor] = cur_city  # 이전 도시 기록
            heapq.heappush(q, (dist_via_cur, neighbor))
    
print(distance[end])

path = [] # 경로 저장
current = end
while current > -1:
    path.append(current)
    current = prev_city[current]

path.reverse()  # 역순(현재 도착지->출발지 순으로 저장되어 있으므로)
print(len(path))
print(*path)