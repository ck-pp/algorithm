from collections import deque

# bfs 정의
def bfs(g):
    q = deque([1])  # 현재 전력망 번호
    visited = set([1])
    cnt = 1  # 현재 연결된 송전탑 개수
    
    while q:
        cur_network = q.popleft()
        
        for neighbor in g[cur_network]:
            if neighbor not in visited:
                q.append((neighbor))
                visited.add(neighbor)
                cnt += 1
                
    return cnt

def solution(n, wires):
    wire_n = len(wires)
    min_diff = 101  # 2-전력망 송전탑 개수 차이 최소값 저장
    
    for i in range(wire_n):
        # 그래프 정의
        g = [[] for _ in range(n+1)]
        
        for j in range(wire_n):
            # 전선 한 개씩 끊어가면서 bfs 실행(= 각 전력망의 연결된 송전탑 개수 카운트)
            if i != j:
                u, v = wires[j]
                
                g[u].append(v)
                g[v].append(u)
        
        networks = bfs(g)  # 1-전력망 송전탑 개수
        anothers = n - networks  # 2-전력망 송전탑 개수
        
        # 2-전력망 송전탑 개수 차이 최소값 업데이트
        min_diff = min(min_diff, abs(networks - anothers))
    
    return min_diff