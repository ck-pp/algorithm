import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque([i for i in range(1, N+1)])

res = []
while len(q) > 0:
    q.rotate(-(K-1))
    res.append(q.popleft())
    
print('<' + ', '.join(map(str, res)) + '>')