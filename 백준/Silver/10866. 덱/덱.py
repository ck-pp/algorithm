import sys
from collections import deque

N = int(sys.stdin.readline())
commands = [sys.stdin.readline().split() for _ in range(N)]
q = deque([])

for cmd in commands:
    if cmd[0] == 'push_front':
        q.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        q.append(cmd[1])
    elif cmd[0] == 'front':
        print(q[0] if len(q) > 0 else -1)
    elif cmd[0] == 'back':
        print(q[-1] if len(q) > 0 else -1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        print(1 if len(q) == 0 else 0)
    elif cmd[0] == 'pop_front':
        print(q.popleft() if len(q) > 0 else -1)
    else:  # pop_back
        print(q.pop() if len(q) > 0 else -1)