import sys
from collections import deque

def bfs(g, start, visited):
    q = deque([start])  # 현재 노드
    
    while q:
        cur_node = q.popleft()
        
        for neighbor in g[cur_node]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)
    
N, M = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

g = [[] for _ in range(N+1)]

for start, end in edges:
    g[start].append(end)
    g[end].append(start)
    
visited = set([])
cnt = 0

for node in range(1, N+1):
    if node not in visited:
        bfs(g, node, visited)
        cnt += 1

print(cnt)