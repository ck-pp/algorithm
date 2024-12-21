import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
commands = [input().split() for _ in range(N)]
q = deque([])

for cmd in commands:
    if cmd[0] == 'push':
        X = int(cmd[1])
        q.append(X)
    elif cmd[0] == 'pop':
        if q: print(q.popleft())
        else: print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if q: print(0)
        else: print(1)
    elif cmd[0] == 'front':
        if q: print(q[0])
        else: print(-1)
    else:
        if q: print(q[-1])
        else: print(-1)