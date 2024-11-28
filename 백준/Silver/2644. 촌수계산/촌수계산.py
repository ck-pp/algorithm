import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
num1, num2 = map(int, input().split())
m = int(input())
parent_childs = [tuple(map(int, input().split())) for _ in range(m)]

g = [[] for _ in range(n+1)]
for x, y in parent_childs:
    g[x].append(y)  # x:부모 y:자식
    g[y].append(x)

def bfs(start, end):
    q = deque([(0, start)])
    visited = set([start])

    while q:
        steps, cur_num = q.popleft()
    
        if cur_num == end:
            return steps
    
        for family_num in g[cur_num]:
            if family_num not in visited:
                q.append((steps + 1, family_num))
                visited.add(family_num)
    
    return -1
    
print(bfs(num1, num2))