import sys
from collections import deque

N = int(sys.stdin.readline())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(N-1)]

root = 1
g = [[] for _ in range(N+1)]

for start, end in edges:
    g[start].append(end)
    g[end].append(start)
    
parents = [-1] * (N+1)
parents[root] = 0  # 루트 노드의 부모는 x
q = deque([root])

while q:
    cur_node = q.popleft()
    
    for neighbor in g[cur_node]:
        if parents[neighbor] == -1:  # 아직 방문하지 않은 노드
            parents[neighbor] = cur_node
            q.append(neighbor)
        
for i in range(2, N+1):
    print(parents[i])