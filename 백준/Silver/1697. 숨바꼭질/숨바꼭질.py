import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

def bfs(start, end):
    q = deque([(0, start)])  # (시간, 위치)
    visited = set([start])

    while q:
        cur_time, cur_pos = q.popleft()
        next_positions = [cur_pos - 1, cur_pos + 1, cur_pos * 2]
    
        if cur_pos == end:
            return cur_time
            
        for next in next_positions:
            if 0 <= next <= 100000 and next not in visited:
                q.append((cur_time + 1, next))
                visited.add(next)
        
print(bfs(N, K))