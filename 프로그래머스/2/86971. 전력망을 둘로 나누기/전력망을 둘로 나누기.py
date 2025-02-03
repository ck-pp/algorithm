from collections import deque
    
def bfs(graph):
    q = deque([1])  # 시작점
    visited = set([1])  # 방문 여부 체크
    cnt = 1  # 개수 카운트
    
    while q:
        node = q.popleft()
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)
                cnt += 1
                
    return cnt
    
def solution(n, wires):
    # 한 쌍씩 빼고 카운트해야 함
    min_diff = n
    for i in range(len(wires)):
        g = [[] for _ in range(n + 1)]
        for j in range(len(wires)):
            if i == j: 
                continue
            
            # i != j일 경우에만 그래프에 노드 쌍 추가
            u, v = wires[j]
            g[u].append(v)
            g[v].append(u)
        
        network = bfs(g)  # 전력망1
        other_network = n - network  # 전력망2
        # 송전탑 개수 차이 최솟값 업데이트
        min_diff = min(min_diff, abs(network - other_network))
    
    return min_diff