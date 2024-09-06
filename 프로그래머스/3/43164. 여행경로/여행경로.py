def dfs(g, node, route):
    while node in g and g[node]:  # 그래프에 node가 있는지 확인해야 함. 안하면 KeyError 발생.
        next_node = g[node].pop()
        dfs(g, next_node, route)
    
    route.append(node)

def solution(tickets):
    route = []  # 스택
    tickets.sort(key=lambda x: x[1], reverse=True)  # 알파벳 순서 앞서는 경로 우선하기 위해
    g = {start: [] for start, _ in tickets}
    
    for start, end in tickets:
        g[start].append(end)
    
    dfs(g, "ICN", route)
    
    return route[::-1]  # 역으로 출력 (재귀 호출이므로)