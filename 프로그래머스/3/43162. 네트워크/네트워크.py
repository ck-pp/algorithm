def solution(n, computers):
    def dfs(node, visited):
        visited[node] = True
        for neighbor in range(n):
            if computers[node][neighbor] == 1 and visited[neighbor] == False:
                dfs(neighbor, visited)
        
    visited = [False] * n
    net_cnt = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i, visited)
            net_cnt += 1
            
    return net_cnt