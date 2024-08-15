from collections import deque

def bfs(node, g, visited):
    queue = deque([node])
    visited[node] = True
    cnt = 1
        
    while queue:
        cur_node = queue.popleft()
        for neighbor in g[cur_node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                cnt += 1
        
    return cnt
    
def solution(n, wires):
    ans = n # 가능한 최대 차이로 초기화
    
    for i in range(len(wires)):
        g = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)

        for j in range(len(wires)):
            if i == j: # # i번째 전선을 끊는다.
                continue
            g[wires[j][0]].append(wires[j][1])
            g[wires[j][1]].append(wires[j][0])
    
        # 첫 번째 네트워크 크기
        cnt1 = bfs(1, g, visited)
        # 두 번째 네트워크 크기
        cnt2 = n - cnt1
        # 두 네트워크의 차이(절댓값)
        difference = abs(cnt1 - cnt2)
        ans = min(ans, difference)
    
    return ans