import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())  # 정점 개수, 간선 개수, 시작 정점
g = [[] for _ in range(N+1)]  # BFS 그래프

# 1. 그래프 초기화
for _ in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

# 2. 정점 번호 내림차순 정렬
for i in range(1, N+1):
    if g[i]:
        g[i].sort(reverse=True)

# 3. bfs 함수 정의
def bfs(start):
    q = deque([start])  # 시작 정점
    visited = set([start])
    steps = [0] * (N + 1)  # 방문 순서 저장

    step_count = 1  # 방문 순서 카운트
    steps[start] = step_count

    while q:
        cur_node= q.popleft()

        for neighbor in g[cur_node]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)
                step_count += 1  # 방문 순서 카운트
                steps[neighbor] = step_count
                
    return steps

# 4. BFS 실행
steps = bfs(R)

# 5. 정점 i의 방문 순서 출력
[print(steps[j]) for j in range(1, N+1)]