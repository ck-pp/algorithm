import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
u_v = [tuple(map(int, input().split())) for _ in range(M)]

# 1. bfs 정의
def bfs(g, ans, start):
    q = deque([start])  # 노드
    steps = 0  # 방문 순서
    visited = set([start])  # 방문 여부 체크
    
    while q:
        cur_node = q.popleft()
        steps += 1  # 방문 순서 카운트
        
        # 오름차순으로 방문
        sorted_nodes = sorted(g[cur_node])
        for next_node in sorted_nodes:
            ans[cur_node] = steps
            # 이동할 수 있는 노드
            if next_node not in visited:
                q.append(next_node)
                visited.add(next_node)
    return

# 2. 그래프 정의
g = [[] for _ in range(N + 1)]
for u, v in u_v:
    g[u].append(v)
    g[v].append(u)

ans = [0 for _ in range(N + 1)]  # ans[i]: 정점 i의 방문 순서
# 3. bfs 실행
bfs(g, ans, R)
# 4. 최소 이동 횟수 출력
for i in range(1, N + 1):
    print(ans[i])