import sys

N, M = map(int, sys.stdin.readline().split())
no_listen = set([sys.stdin.readline().strip() for _ in range(N)])
no_see = set([sys.stdin.readline().strip() for _ in range(M)])

no_listen_see = sorted(list(no_listen & no_see))
print(len(no_listen_see))
for name in no_listen_see:
    print(name)