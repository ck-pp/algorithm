import sys
from collections import deque
# BFS로 풀이해보기 -> 가중치가 다 같기 때문에 이게 더 효율적

input = sys.stdin.readline

N, M, K, X = map(int, input().split())  # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
A_B_lists = [list(map(int, input().split())) for _ in range(M)]

g = [[] for _ in range(N + 1)]
for A, B in A_B_lists:
    g[A].append(B)
    
q = deque([X])  # (거리, 시작 도시)
distance = [-1] * (N + 1)  # -1: 방문하지 않은 노드
distance[X] = 0

while q:
    cur_city = q.popleft()
    
    for neighbor in g[cur_city]:
        if distance[neighbor] == -1:  # 방문하지 않은 노드만 탐색
            q.append(neighbor)
            distance[neighbor] = distance[cur_city] + 1

# X로부터 최단 거리가 K인 도시 번호만 추가
result = [idx for idx, dist in enumerate(distance) if dist == K]

if result:
    print(*result)  # 리스트 그대로 출력
else:
    print(-1)