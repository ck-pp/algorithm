from collections import deque

def solution(n, vertex):
    # 1번 노드로부터 ~ : 다익스트라인줄 알았는데 BFS가 더 효율적이다. 가중치가 없기 때문에.
    g = [[] for _ in range(n + 1)]
    
    for a, b in vertex:
        g[a].append(b)
        g[b].append(a)
    
    distance = [-1] * (n + 1)  # 모든 노드 거리 -1로 초기화
    distance[1] = 0
    q = deque([1])  # 1번 노드가 시작점
    
    while q:
        cur_node = q.popleft()
        
        for neighbor in g[cur_node]:
            if distance[neighbor] == -1:  # 아직 방문하지 않은 노드라면
                distance[neighbor] = distance[cur_node] + 1
                q.append(neighbor)
    
    return distance.count(max(distance))