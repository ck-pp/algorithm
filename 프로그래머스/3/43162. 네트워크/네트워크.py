from collections import deque

def solution(n, computers):
    visited = [False] * n
    net_cnt = 0
    
    def bfs(start):
        q = deque([start])
        visited[start] = True
    
        while q:
            cur_node = q.popleft()
            for i in range(n):
                # 연결된 컴퓨터 중 방문하지 않은 컴퓨터 큐에 추가
                if computers[cur_node][i] == 1 and not visited[i]:
                    visited[i] = True
                    q.append(i)
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            net_cnt += 1
    
    return net_cnt