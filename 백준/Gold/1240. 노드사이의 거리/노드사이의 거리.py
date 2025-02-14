import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())  # 노드의 개수, 거리 알고 싶은 노드 쌍 개수

# 그래프 초기화
g = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v, w = map(int, input().split())
    g[u].append((v, w))
    g[v].append((u, w))
    
node_pairs = [tuple(map(int, input().split())) for _ in range(M)]

# bfs 정의
def bfs(u, v):
    q = deque([(u, 0)])  # (현재 노드, 거리)
    visited = set([u])  # 방문 여부 체크
    
    while q:
        cur_node, dist = q.popleft()
        
        if cur_node == v:  # 현재 노드가 도착 노드일 경우
            return dist
            
        for neighbor, w in g[cur_node]:
            if neighbor not in visited:
                q.append((neighbor, dist + w))
                visited.add(neighbor)

# bfs 실행
for u, v in node_pairs:
    print(bfs(u, v))  # 두 노드 사이의 거리 출력