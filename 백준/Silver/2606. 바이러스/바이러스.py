import sys
from collections import deque

computer_num = int(sys.stdin.readline())
computer_pair_num = int(sys.stdin.readline())
computer_pairs = [list(map(int, sys.stdin.readline().split())) for _ in range(computer_pair_num)]

g = [[] for _ in range(computer_num + 1)]
for u, v in computer_pairs:
    g[u].append(v)
    g[v].append(u)
    
q = deque([1])  # 1번 컴퓨터에서 시작
visited = set([1])
cnt = 0

while q:
    cur_computer = q.popleft()
    
    for neighbor in g[cur_computer]:
        if neighbor not in visited:
            q.append(neighbor)
            visited.add(neighbor)
            cnt += 1  # 연결된 컴퓨터 수 카운트

print(cnt)