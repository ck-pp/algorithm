import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())

def bfs(start, end):
    q = deque([(0, start)])  # (연산 횟수, 값)
    visited = set([start])
    
    while q:
        steps, cur_num = q.popleft()

        if cur_num == end:
            return steps + 1
    
        next_nums = [cur_num * 2, cur_num * 10 + 1]
        for next_num in next_nums:
            if next_num <= end and next_num not in visited:  # next_num <= end 조건 왜 생각을 못했지! 멍청이!
                q.append((steps + 1, next_num))
                visited.add(next_num)
                
    return -1

print(bfs(A, B))