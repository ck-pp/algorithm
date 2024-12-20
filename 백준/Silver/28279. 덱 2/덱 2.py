import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
commands = [input().split() for _ in range(N)]
dq = deque([])

for command in commands:
    cmd = int(command[0])
    if cmd == 1:
        dq.appendleft(int(command[1]))
    elif cmd == 2:
        dq.append(int(command[1]))
    elif cmd == 3:
        if dq: print(dq.popleft())
        else: print(-1)
    elif cmd == 4:
        if dq: print(dq.pop())
        else: print(-1)
    elif cmd == 5:
        print(len(dq))
    elif cmd == 6:
        if dq: print(0)
        else: print(1)
    elif cmd == 7:
        if dq: print(dq[0])
        else: print(-1)
    else:
        if dq: print(dq[-1])
        else: print(-1)