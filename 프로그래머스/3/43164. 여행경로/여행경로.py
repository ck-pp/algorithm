from collections import defaultdict

def dfs(graph, node, route):
        while graph[node]:
            next_node = graph[node].pop()
            dfs(graph, next_node, route)
        route.append(node)

def solution(tickets):
    route = []
    # 그래프 생성
    graph = defaultdict(list)
    
    for start, end in tickets:
        graph[start].append(end)
    
    # 도착지 사전순 정렬 _ 제한사항 조건 충족 위해
    for key in graph:
        graph[key].sort(reverse=True) # pop -> 역순 정렬
    
    dfs(graph, "ICN", route)    
    
    return route[::-1] # 재귀 > 방문 경로 역순으로 저장 > 뒤집어서 반환