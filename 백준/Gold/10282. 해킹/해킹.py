import sys
import heapq
input = sys.stdin.readline

# 1. 테스트케이스 수만큼 반복
T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())  # 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터의 번호
    g = [[] for _ in range(n+1)]
    
    for _ in range(d):
        # 컴퓨터 a가 컴퓨터 b를 의존하며, 컴퓨터 b가 감염되면 s초 후 컴퓨터 a도 감염됨
        a, b, s = map(int, input().split())
        g[b].append((a, s))
        
    # 가중치가 다르므로 다익스트라 적용
    distance = [float('INF')] * (n+1)
    distance[c] = 0
    q = [(0, c)]  # (감염되기까지 걸리는 시간, 감염된 컴퓨터 번호)
    
    while q:
        cur_time, cur_computer = heapq.heappop(q)
        
        # 이미 감염 시간이 최소인 경우
        if cur_time > distance[cur_computer]:
            continue
        
        for neighbor, t in g[cur_computer]:
            if distance[neighbor] > cur_time + t:
                distance[neighbor] = cur_time + t
                heapq.heappush(q, (distance[neighbor], neighbor))
    
    # 감염된 컴퓨터 개수
    infected_computers = sum(1 for d in distance if d != float('INF'))
    # 마지막 컴퓨터가 감염되기까지 걸리는 시간
    last_infection_time = max([d for d in distance if d != float('INF')], default=0)
    
    
    # 4. 결과값 출력
    print(infected_computers, last_infection_time)