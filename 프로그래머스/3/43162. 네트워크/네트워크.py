from collections import deque

# bfs 정의
def bfs(g, q, visited):
    while q:
        cur_computer = q.popleft()
        
        for next_computer in g[cur_computer]:
            if next_computer not in visited:
                q.append(next_computer)
                visited.add(next_computer)
    
    return 1

def solution(n, computers):
    # 네트워크 개수 > 모두 탐색할 필요x > bfs
    networks = 0
    
    # A-B, B-C == A-B-C
    g = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                g[i+1].append(j+1)  # 인덱스는 0부터~이므로 컴퓨터 번호 1부터~로 맞춰줌
                    
    q = deque([])
    visited = set([])
    
    for i in range(1, n+1):
        # 방문하지 않은 컴퓨터일 경우
        if i not in visited:
            q.append(i)
            visited.add(i)
            # bfs 실행 == 네트워크 개수 더하기
            networks += bfs(g, q, visited)
    
    return networks