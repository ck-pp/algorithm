import heapq as hq

def solution(N, road, K):
    # 그래프 정의
    g = [[] for _ in range(N + 1)]
    for u, v, time in road:
        g[u].append((v, time))
        g[v].append((u, time))
        
    # 1번 마을에서 각 마을까지 가는데 걸리는 시간(가중치) 저장 배열
    distance = [float('INF')] * (N + 1)
    distance[1] = 0
    
    # 우선순위 큐 (min-heap) 사용
    q = [(0, 1)]  # (시간(w), 현재 마을(node))
    
    while q:
        cur_dist, cur_node = hq.heappop(q)
        
        # 이미 가중치가 최소인 경우 건너뛰기
        if distance[cur_node] < cur_dist:
            continue
        
        for neighbor, w in g[cur_node]:
            dist_via_cur = cur_dist + w
            
            # 더 짧은 경로를 찾은 경우 갱신
            if dist_via_cur < distance[neighbor]:
                distance[neighbor] = dist_via_cur
                hq.heappush(q, (dist_via_cur, neighbor))

    # 1번 마을로부터 음식 배달 시간이 K 이하인 마을 개수 출력
    return sum(1 for t in distance if t <= K)