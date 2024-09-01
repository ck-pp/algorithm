import heapq

def solution(N, road, K):
    g = [[] for _ in range(N + 1)]
    
    for a, b, c in road:
        g[a].append((b, c))
        g[b].append((a, c))
    
    distance = [float('inf')] * (N + 1)
    distance[1] = 0  # 1번 마을에서 시작
    
    # 우선순위 큐 (min-heap) 사용
    q = [(0, 1)]  # (거리, 노드)
    
    while q:
        cur_dist, cur_node = heapq.heappop(q)
        
        # 이미 더 짧은 경로를 알고 있는 경우 무시
        if cur_dist > distance[cur_node]:
            continue
        
        # 현재 노드와 연결된 다른 노드 검사
        for neighbor, weight in g[cur_node]:
            dist_via_cur = cur_dist + weight
            
            # 더 짧은 경로를 찾은 경우 갱신
            if dist_via_cur < distance[neighbor]:
                distance[neighbor] = dist_via_cur
                heapq.heappush(q, (dist_via_cur, neighbor))

    return sum(1 for d in distance if d <= K)