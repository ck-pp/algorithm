from collections import defaultdict

# dfs 정의
def dfs(g, node, route):
    while g[node]:
        next_node = g[node].pop()
        dfs(g, next_node, route)
    
    route.append(node)
    
def solution(tickets):
    graph = defaultdict(list)
    # pop은 오른쪽부터이므로 내림차순 정렬
    tickets.sort(key=lambda city:city[1], reverse=True)
    
    # 경로 그래프 저장
    for u, v in tickets:
        graph[u].append(v)

    route = []
    # dfs 로직 실행
    dfs(graph, "ICN", route)
    
    # 재귀 호출 -> 역으로 출력
    return route[::-1]