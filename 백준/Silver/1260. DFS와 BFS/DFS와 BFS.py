import sys
from collections import deque

def dfs(g, start):
    stack = [start]
    visited = set()  # 집합으로 방문 여부 확인
    res = []

    while stack:
        cur_node = stack.pop()

        if cur_node not in visited:
            visited.add(cur_node)
            res.append(cur_node)
            # 스택에 이웃 노드를 추가할 때 내림차순으로 정렬하여 큰 노드부터 넣음
            stack.extend(sorted(g[cur_node], reverse=True))
            
    return res
    
def bfs(g, start):
    q = deque([start])
    visited = set([start])
    res = [start]
    
    while q:
        cur_node = q.popleft()

        for neighbor in sorted(g[cur_node]):  # 이웃 노드를 오름차순으로 정렬하여 작은 노드부터 탐색
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)
                res.append(neighbor)
                    
    return res

N, M, V = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

g = [[] for _ in range(N+1)]
for u, v in edges:
    g[u].append(v)
    g[v].append(u)

print(*dfs(g, V))
print(*bfs(g, V))