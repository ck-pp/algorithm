# 최단경로 -> BFS / 다익스트라
# 가중치 X 이므로, BFS 사용

from collections import deque

def solution(n, vertex):
    
    g = [[] for _ in range(n + 1)]
    
    distance = [-1] * (n + 1)  # 이걸로 방문 여부 파악, -1은 아직 방문하지 않았다는 의미
    distance[1] = 0  # 1 -> 1은 0이므로
    q = deque([1])  # (노드)
    
    for start, end in vertex:
        g[start].append(end)
        g[end].append(start)
        
    while q:
        cur_node = q.popleft()
         
        for neighbor in g[cur_node]:
            if distance[neighbor] == -1:
                q.append(neighbor)
                distance[neighbor] = distance[cur_node] + 1
    
    return distance.count(max(distance))